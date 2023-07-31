from ultralytics import YOLO

# upload model to train from scratch
model = YOLO('yolov8s.yaml')

# upload a model from weights
# model = YOLO('/home/martinson/runs/detect/train: x; high_aug/weights/last.pt')

# train
results = model.train(
    data='/home/martinson/data_2/dataset.yaml',
    name="train: s; ...",
    epochs=100,
    patience=0,
    # cfg="/home/martinson/config_high_aug.yaml",
)