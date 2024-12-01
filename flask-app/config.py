# Configuration settings
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mysecretkey')
    CAMERA_INDEX = 0
