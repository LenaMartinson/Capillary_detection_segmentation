from ultralytics import YOLO

# file to see results of detection YOLOv8 in console
folder_name = "/home/martinson/runs/detect/train: s; no-augmentations-hyp_1; patience=0/weights/"

params = {
    "imgsz": 640,
}

model = YOLO(folder_name + "last.pt")
results_val = model.val(**params).box.p[1]
results_test = model.val(split='test', **params).box.p[1]

model_2 = YOLO(folder_name + "best.pt")
results_val_2 = model_2.val(**params).box.p[1]
results_test_2 = model_2.val(split='test', **params).box.p[1]

print("Best")
print("Val (sharp precision):", results_val_2)
print("Test (sharp precision):", results_test_2)

print("Last")
print("Val (sharp precision):", results_val)
print("Test (sharp precision):", results_test)