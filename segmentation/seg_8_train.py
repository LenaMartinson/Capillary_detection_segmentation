from ultralytics import YOLO

# upload model to train from scratch
model = YOLO('yolov8s-seg.yaml')

# upload a model from weights
# model = YOLO('/home/martinson/runs/segment/seg; train s; big_data; mech_aug/weights/last.pt')

model.train(
    data='/home/martinson/data_small/dataset.yaml',
    name='seg; train s; ...',
    epochs=100,
    # imgsz=640,
    device=0,
    # cfg='/home/martinson/config_no_aug.yaml'
)
