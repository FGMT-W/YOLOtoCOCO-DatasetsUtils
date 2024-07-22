import os

# 数据集路径
dataset_path = 'C:/Users/thefr/Desktop/datasets'
# 标签文件夹路径
labels_path = os.path.join(dataset_path, 'labels')
# 图像文件夹路径
images_path = os.path.join(dataset_path, 'images')

# 设置要查找的标签类别
target_label = '14'

# 用于存储包含目标标签的图像文件名
images_with_target_label = []

# 遍历标签文件夹中的所有标签文件
for label_file_name in os.listdir(labels_path):
    label_file_path = os.path.join(labels_path, label_file_name)

    if label_file_name.endswith('.txt'):
        with open(label_file_path, 'r') as file:
            lines = file.readlines()

        # 检查文件中是否存在类别3的标注
        for line in lines:
            parts = line.split()
            if parts[0] == target_label:
                image_file_name = label_file_name.replace('.txt', '.jpg')
                image_file_path = os.path.join(images_path, image_file_name)
                if os.path.exists(image_file_path):
                    images_with_target_label.append(image_file_name)
                break

# 打印包含目标标签的图像文件名
print("Images with target label:")
for image in images_with_target_label:
    print(image)
