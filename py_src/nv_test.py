from yolov4.tf import YOLOv4
import os 

cur_dir = "/home/nikoenki/Documents/yolov4/tensorflow-yolov4/py_src/"

yolo = YOLOv4()
yolo.classes = os.path.join(cur_dir,"coco.names")
yolo.input_size = (640, 480)

yolo.make_model()

yolo.load_weights("yolov4.weights", weights_type="yolo")
pict = os.path.join(cur_dir, ".." , "test","kite.jpg")
yolo.inference(media_path= pict)

