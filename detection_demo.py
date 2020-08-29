import os

os.environ['CUDA_VISIBLE_DEVICES'] = '0'
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.python.saved_model import tag_constants
from yolov3.yolov3 import Create_Yolov3
from yolov3.utils import load_yolo_weights, detect_image
from yolov3.config import *

image_path = "./data/images/kite.jpg"

Darknet_weights = YOLO_V3_WEIGHTS

yolo = Create_Yolov3(input_size=YOLO_INPUT_SIZE, CLASSES=YOLO_COCO_CLASSES)
load_yolo_weights(yolo, Darknet_weights)  # use Darknet weights

detect_image(yolo, image_path, "./data/images/pred_kite.jpg", input_size=YOLO_INPUT_SIZE, show=True, rectangle_colors=(255, 0, 0))
