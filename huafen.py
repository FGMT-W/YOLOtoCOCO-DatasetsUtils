import os
import random
import shutil

# 设置数据集路径
dataset_path = "C:/Users/thefr/Desktop/datasetsYOLOV1"
images_path = os.path.join(dataset_path, "images")
labels_path = os.path.join(dataset_path, "labels")

# 创建训练集、验证集和测试集目录
train_path = os.path.join(dataset_path, "train")
val_path = os.path.join(dataset_path, "val")
test_path = os.path.join(dataset_path, "test")
os.makedirs(train_path, exist_ok=True)
os.makedirs(test_path, exist_ok=True)

# 获取所有图像和标签文件的路径
images = os.listdir(images_path)
labels = os.listdir(labels_path)
# 确保图像和标签文件数量一致
assert len(images) == len(labels)

# 将文件名列表随机排序
random.shuffle(images)

# 计算训练集、验证集和测试集的数量
total_size = len(images)
train_size = int(0.7 * total_size)
val_size = int(0.2 * total_size)
test_size = total_size - train_size - val_size

# 创建训练集、验证集和测试集目录
train_images_path = os.path.join(train_path, "images")
train_labels_path = os.path.join(train_path, "labels")
os.makedirs(train_images_path, exist_ok=True)
os.makedirs(train_labels_path, exist_ok=True)

val_images_path = os.path.join(val_path, "images")
val_labels_path = os.path.join(val_path, "labels")
os.makedirs(val_images_path, exist_ok=True)
os.makedirs(val_labels_path, exist_ok=True)

test_images_path = os.path.join(test_path, "images")
test_labels_path = os.path.join(test_path, "labels")
os.makedirs(test_images_path, exist_ok=True)
os.makedirs(test_labels_path, exist_ok=True)

# 复制训练集图像和标签文件到train目录
for i in range(train_size):
    image_name = images[i]
    label_name = image_name.replace(".jpg", ".txt")
    src_image = os.path.join(images_path, image_name)
    src_label = os.path.join(labels_path, label_name)
    dst_image = os.path.join(train_images_path, image_name)
    dst_label = os.path.join(train_labels_path, label_name)
    shutil.copyfile(src_image, dst_image)
    shutil.copyfile(src_label, dst_label)

# 复制验证集图像和标签文件到val目录
for i in range(train_size, train_size + val_size):
    image_name = images[i]
    label_name = image_name.replace(".jpg", ".txt")
    src_image = os.path.join(images_path, image_name)
    src_label = os.path.join(labels_path, label_name)
    dst_image = os.path.join(val_images_path, image_name)
    dst_label = os.path.join(val_labels_path, label_name)
    shutil.copyfile(src_image, dst_image)
    shutil.copyfile(src_label, dst_label)

# 复制测试集图像和标签文件到test目录
for i in range(train_size + val_size, total_size):
    image_name = images[i]
    label_name = image_name.replace(".jpg", ".txt")
    src_image = os.path.join(images_path, image_name)
    src_label = os.path.join(labels_path, label_name)
    dst_image = os.path.join(test_images_path, image_name)
    dst_label = os.path.join(test_labels_path, label_name)
    shutil.copyfile(src_image, dst_image)
    shutil.copyfile(src_label, dst_label)

print("数据集已成功划分为训练集、验证集和测试集！")