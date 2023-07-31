import yolov5.segment.train

# how to train YOLOv5 segmentation model from scratch
yolov5.segment.train.run(
    data='/home/martinson/data_2/dataset_seg.yaml',
    name='seg; train s; no_aug',
    weights='',
    cfg='yolov5s-seg.yaml',
    device=0,
    epochs=100,
    hyp='/home/martinson/yolov5/data/hyps/hyp.no-augmentation.yaml',
)
