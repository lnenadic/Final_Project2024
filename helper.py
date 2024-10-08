from ultralytics import YOLO
import streamlit as st
import cv2
import settings
import PIL


def load_model(model_path):
    model = YOLO(model_path)
    return model


def _display_detected_frames(conf, model, st_frame, image):
    # Resize the image to a standard size
    image = cv2.resize(image, (720, int(720*(9/16))))

    # Predict the objects in the image using the YOLOv8 model
    res = model.predict(image, conf=conf)

    # Plot the detected objects on the video frame
    res_plotted = res[0].plot()
    st_frame.image(res_plotted,
                   caption='Detected Video',
                   channels="BGR",
                   use_column_width=True
                   )


def play_stored_video(conf, model):
    source_vid = st.sidebar.selectbox(
        "Choose a video...", settings.VIDEOS_DICT.keys())
    with open(settings.VIDEOS_DICT.get(source_vid), 'rb') as video_file:
        video_bytes = video_file.read()

    if video_bytes:
        st.video(video_bytes)
    if st.sidebar.button('Detect Video Objects'):
        try:
            vid_cap = cv2.VideoCapture(
                str(settings.VIDEOS_DICT.get(source_vid)))
            st_frame = st.empty()
            while (vid_cap.isOpened()):
                success, image = vid_cap.read()
                if success:
                    _display_detected_frames(conf,
                                             model,
                                             st_frame,
                                             image,
                                             )
                else:
                    vid_cap.release()
                    break
        except Exception as e:
            st.sidebar.error("Error loading video: " + str(e))


def play_webcam(conf, model):
    # Use the st.camera_input widget to capture an image from the webcam
    st.markdown("<h2>Webcam Feed</h2>", unsafe_allow_html=True)

    # Capture an image from the webcam
    img_data = st.camera_input("Capture an image")

    if img_data is not None:
        # Open the image with PIL
        uploaded_image = PIL.Image.open(img_data)

        # Perform object detection using the YOLOv8 model
        res = model.predict(uploaded_image, conf=conf)
        res_plotted = res[0].plot()[:, :, ::-1]

        # Display the detected objects
        st.image(res_plotted, caption='Detected Image', use_column_width=True)

        try:
            with st.expander("Detection Results"):
                boxes = res[0].boxes
                for box in boxes:
                    st.write(box.data)
        except Exception as ex:
            st.error("Error processing detection results.")
            st.error(ex)
