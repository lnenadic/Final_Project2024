# settings for the project, including model paths, thresholds, object names, and Streamlit app

from pathlib import Path
import sys

# Get the absolute path of the current file
FILE = Path(__file__).resolve()
# Get the parent directory of the current file
ROOT = FILE.parent
# Add the root path to the sys.path list if it is not already there
if ROOT not in sys.path:
    sys.path.append(str(ROOT))
# Get the relative path of the root directory with respect to the current working directory
ROOT = ROOT.relative_to(Path.cwd())

# Sources
IMAGE = 'Image'
VIDEO = 'Video'
WEBCAM = 'Webcam'

SOURCES_LIST = [IMAGE, VIDEO, WEBCAM]

# Images config
IMAGES_DIR = ROOT / 'images'
DEFAULT_IMAGE = IMAGES_DIR / 'img-1.jpg'
DEFAULT_DETECT_IMAGE = IMAGES_DIR / 'img-1-detected.jpg'

# Videos config
VIDEO_DIR = ROOT / 'videos'
VIDEOS_DICT = {
    'vid_1': VIDEO_DIR / 'vid_1.mp4',
    'vid_2': VIDEO_DIR / 'vid_2.mp4',
}

# ML Model config
MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = MODEL_DIR / 'custom-model.pt'
SEGMENTATION_MODEL = MODEL_DIR / 'custom-seg.pt'

# Webcam
WEBCAM_PATH = 0
