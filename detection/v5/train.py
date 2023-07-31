import yolov5.train

# train
yolov5.train.run(
    data='data_2/dataset.yaml',
    name='train n; ...',
    # weights='/home/martinson/yolov5/runs/train/train x; high-aug2/weights/last.pt',
    cfg='yolov5n.yaml',
    device=0,
    epochs=100,
    # imgsz=640,
    # hyp='/home/martinson/yolov5/data/hyps/hyp.no-augmentation.yaml'
)
