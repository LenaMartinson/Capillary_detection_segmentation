# file to change names in my folder
with open("/home/martinson/data_2/train.txt") as f:
    all_lines = f.readlines()
    with open("/home/martinson/data_2/train2.txt", "w") as new_f:
        for i in all_lines:
            new_line = i.replace("\\", "/")
            new_line = new_line.replace(r"C:/Users/Alex/Code/MayFinetudeWideDetection/reviewed_ds_13-06-23-II", "/home/martinson/data_2")
            new_f.write(new_line)

with open("/home/martinson/data_2/val.txt") as f:
    all_lines = f.readlines()
    with open("/home/martinson/data_2/val2.txt", "w") as new_f:
        for i in all_lines:
            new_line = i.replace("\\", "/")
            new_line = new_line.replace(r"C:/Users/Alex/Code/MayFinetudeWideDetection/reviewed_ds_13-06-23-II", "/home/martinson/data_2")
            new_f.write(new_line)

with open("/home/martinson/data_2/test.txt") as f:
    all_lines = f.readlines()
    with open("/home/martinson/data_2/test2.txt", "w") as new_f:
        for i in all_lines:
            new_line = i.replace("\\", "/")
            new_line = new_line.replace(r"C:/Users/Alex/Code/MayFinetudeWideDetection/reviewed_ds_13-06-23-II", "/home/martinson/data_2")
            new_f.write(new_line)

with open("/home/martinson/data_2/all.txt") as f:
    all_lines = f.readlines()
    with open("/home/martinson/data_2/all2.txt", "w") as new_f:
        for i in all_lines:
            new_line = i.replace("\\", "/")
            new_line = new_line.replace(r"C:/Users/Alex/Code/MayFinetudeWideDetection/reviewed_ds_13-06-23-II", "/home/martinson/data_2")
            new_f.write(new_line)