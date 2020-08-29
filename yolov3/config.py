# YOLO options
YOLO_FRAMEWORK              = "tf"
YOLO_TYPE                   = "yolov3" # yolov4 or yolov3
YOLO_V3_WEIGHTS             = "models/yolov3.weights"
YOLO_COCO_CLASSES              = "models/coco/coco.names"
YOLO_STRIDES              = [8, 16, 32]
YOLO_ANCHOR_PER_SCALE     = 3
YOLO_IOU_LOSS_THRESH      = 0.5
YOLO_MAX_BBOX_PER_SCALE     = 100
YOLO_INPUT_SIZE             = 416

YOLO_ANCHORS            = [[[10,  13], [16,   30], [33,   23]],
                               [[30,  61], [62,   45], [59,  119]],
                               [[116, 90], [156, 198], [373, 326]]]


download_yolov3_weights = "https://pjreddie.com/media/files/yolov3.weights"

