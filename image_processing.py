import cv2
import numpy as np
import tensorflow as tf

MODEL_PATH = "D:\Project\ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8 (1)\ssd_mobilenet_v2_fpnlite_640x640_coco17_tpu-8\saved_model"
LABEL_MAP_PATH = "D:\Project\mscoco_label_map.pbtxt"

KNOWN_WIDTH = 24.0  # Known width of the object in inches
FOCAL_LENGTH = 600  # Approximate focal length in pixels (calibrated)
STEP_LENGTH = 30.0  # Average step length in inches

model = tf.saved_model.load(MODEL_PATH)

category_index = {}
with open(LABEL_MAP_PATH, 'r') as f:
    lines = f.readlines()
    for line in lines:
        if "id" in line:
            item_id = int(line.strip().split(": ")[1])
        if "name" in line:
            item_name = line.strip().split(": ")[1].replace("'", "")
            category_index[item_id] = item_name

def calculate_distance(known_width, focal_length, width_in_pixels):
    if width_in_pixels == 0:
        return float('inf')
    return (known_width * focal_length) / width_in_pixels

def detect_objects(image):
    input_tensor = tf.convert_to_tensor(image)
    input_tensor = input_tensor[tf.newaxis, ...]

    detections = model(input_tensor)
    num_detections = int(detections.pop('num_detections'))
    detections = {key: value[0, :num_detections].numpy() for key, value in detections.items()}
    detections['detection_classes'] = detections['detection_classes'].astype(np.int64)
    detected_objects = []

    height, width = image.shape[:2]

    for i in range(num_detections):
        if detections['detection_scores'][i] > 0.5:
            class_id = detections['detection_classes'][i]
            class_name = category_index.get(class_id, "Unknown")
            box = detections['detection_boxes'][i]
            x1, x2 = int(box[1] * width), int(box[3] * width)
            width_in_pixels = x2 - x1

            distance = calculate_distance(KNOWN_WIDTH, FOCAL_LENGTH, width_in_pixels)
            detected_objects.append((class_name, distance))

    return detected_objects

def capture_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if ret:
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame_rgb
    else:
        raise Exception("Failed to capture image")