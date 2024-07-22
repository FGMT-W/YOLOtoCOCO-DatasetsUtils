import os
import random


def delete_random_images_and_labels(image_dir, label_dir, num_to_delete):
    # 获取图片和标签文件目录下的所有文件名
    image_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg')]
    label_files = [f for f in os.listdir(label_dir) if f.endswith('.txt')]

    # 确保标签文件和图片文件数量一致
    image_files_set = set(image_files)
    label_files_set = set(label_files)
    if not all(img_file.replace('.jpg', '.txt') in label_files_set for img_file in image_files):
        raise ValueError("Image and label files do not match!")

    # 确定可以删除的图片文件
    if num_to_delete > len(image_files):
        raise ValueError("Number of files to delete exceeds the number of available images.")

    files_to_delete = random.sample(image_files, num_to_delete)

    deleted_files = []

    for img_file in files_to_delete:
        # 生成对应的标签文件名
        txt_file = img_file.replace('.jpg', '.txt')

        # 删除图片文件
        img_file_path = os.path.join(image_dir, img_file)
        os.remove(img_file_path)
        deleted_files.append(img_file_path)
        print(f"Deleted image file: {img_file_path}")

        # 删除标签文件
        txt_file_path = os.path.join(label_dir, txt_file)
        os.remove(txt_file_path)
        deleted_files.append(txt_file_path)
        print(f"Deleted label file: {txt_file_path}")

    return deleted_files


# 使用示例
image_directory = "C:/Users/thefr/Desktop/绿光-白天15m/images"  # 替换为你的图片文件目录路径
label_directory = "C:/Users/thefr/Desktop/绿光-白天15m/labels"  # 替换为你的标签文件目录路径
number_to_delete = 1254  # 替换为你要删除的图片和标签文件的数量

deleted_files = delete_random_images_and_labels(image_directory, label_directory, number_to_delete)
print(f"Total deleted files: {len(deleted_files)}")
