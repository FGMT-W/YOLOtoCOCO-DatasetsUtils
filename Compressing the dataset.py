import os
import random
import shutil
from collections import defaultdict

# 设置图片和标签文件夹路径
image_dir = 'C:/Users/thefr/Desktop/datasetsV7/test/images'
label_dir = 'C:/Users/thefr/Desktop/datasetsV7/test/labels'
num_to_delete = 2799

# 获取所有图片和标签文件列表
images = [f for f in os.listdir(image_dir) if f.endswith('.jpg')]
labels = [f for f in os.listdir(label_dir) if f.endswith('.txt')]

# 确保图片和标签文件数量一致
assert len(images) == len(labels), "图片和标签文件数量不一致"

# 构建图片与标签的对应关系
image_label_pairs = list(zip(images, labels))

# 检查图片中包含的标签类别分布
def get_label_distribution(label_dir, labels):
    label_count = defaultdict(int)
    for label_file in labels:
        with open(os.path.join(label_dir, label_file), 'r') as f:
            for line in f:
                label_id = int(line.split()[0])
                label_count[label_id] += 1
    return label_count

# 删除指定数量的图片及其标签文件
def delete_files(image_label_pairs, num_to_delete):
    to_delete = random.sample(image_label_pairs, num_to_delete)
    for image_file, label_file in to_delete:
        os.remove(os.path.join(image_dir, image_file))
        os.remove(os.path.join(label_dir, label_file))
    return to_delete

# 获取初始标签分布
initial_distribution = get_label_distribution(label_dir, labels)
print("Initial label distribution:", initial_distribution)

# 删除文件
deleted_files = delete_files(image_label_pairs, num_to_delete)

# 获取删除后的标签分布
remaining_images = [f for f in os.listdir(image_dir) if f.endswith('.jpg')]
remaining_labels = [f for f in os.listdir(label_dir) if f.endswith('.txt')]
remaining_distribution = get_label_distribution(label_dir, remaining_labels)
print("Remaining label distribution:", remaining_distribution)

# 输出删除的文件列表
print("Deleted files:", deleted_files)
