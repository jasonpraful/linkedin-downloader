
import os

# EDIT
USERNAME = ''
PASSWORD = ''
DIR = 'downloaded_videos'
##example -
##URL = https://www.linkedin.com/learning/machine-learning-and-ai-foundations-predictive-modeling-strategy-at-scale/scaling-machine-learning-initiatives

## Courses = [
#       'machine-learning-and-ai-foundations-predictive-modeling-strategy-at-scale'
#]
COURSES = [
#insert slugs here

]

# EDIT IF YOU NEED TO
BASE_DOWNLOAD_PATH = os.path.join(os.path.dirname(__file__), DIR)
USE_PROXY = False
PROXY = "http://127.0.0.1:8888" if USE_PROXY else None
