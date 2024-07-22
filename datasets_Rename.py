import os
import shutil

def check_and_rename_yolo_files(images_path, labels_path, new_images_path, new_labels_path, start_index):
    # 获取所有jpg和txt文件名
    image_files = sorted([f for f in os.listdir(images_path) if f.endswith('.jpg')])
    label_files = sorted([f for f in os.listdir(labels_path) if f.endswith('.txt')])

    # 去除扩展名，只保留文件名部分
    image_files_no_ext = [os.path.splitext(f)[0] for f in image_files]
    label_files_no_ext = [os.path.splitext(f)[0] for f in label_files]

    # 找出没有对应标签的图片文件
    unmatched_images = [f + '.jpg' for f in image_files_no_ext if f not in label_files_no_ext]
    unmatched_labels = [f + '.txt' for f in label_files_no_ext if f not in image_files_no_ext]

    if unmatched_images or unmatched_labels:
        print("以下JPG文件没有对应的标签文件：")
        for img in unmatched_images:
            print(img)
        print("以下TXT文件没有对应的图片文件：")
        for lbl in unmatched_labels:
            print(lbl)
        return

    # 创建新的文件夹，如果不存在的话
    os.makedirs(new_images_path, exist_ok=True)
    os.makedirs(new_labels_path, exist_ok=True)

    # 重命名并移动文件
    for i, (img_file, lbl_file) in enumerate(zip(image_files, label_files)):
        new_img_name = f"frame_{start_index + i}.jpg"
        new_lbl_name = f"frame_{start_index + i}.txt"

        shutil.copy2(os.path.join(images_path, img_file), os.path.join(new_images_path, new_img_name))
        shutil.copy2(os.path.join(labels_path, lbl_file), os.path.join(new_labels_path, new_lbl_name))

    print(f"所有文件已成功重命名并保存到新文件夹中。")

# 使用示例
images_path = 'C:/Users/thefr/Desktop/images'
labels_path = 'C:/Users/thefr/Desktop/labels'
new_images_path = 'C:/Users/thefr/Desktop/绿光-白天20m/images'
new_labels_path = 'C:/Users/thefr/Desktop/绿光-白天20m/labels'
start_index = 32522  # 从指定数字开始自增

check_and_rename_yolo_files(images_path, labels_path, new_images_path, new_labels_path, start_index)
