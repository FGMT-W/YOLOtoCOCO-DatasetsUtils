import os

# 数据集路径
#dataset_path = 'C:/Users/thefr/Desktop/AG_Result/'
# 图像文件夹路径
images_path = os.path.join('C:/Users/thefr/Desktop/datasetsYOLOV3/images/val')
# 标签文件夹路径
labels_path = os.path.join('C:/Users/thefr/Desktop/datasetsYOLOV3/labels/val')

# 获取所有图像和标签文件名
image_files = set(os.path.splitext(f)[0] for f in os.listdir(images_path) if f.endswith('.jpg'))
label_files = set(os.path.splitext(f)[0] for f in os.listdir(labels_path) if f.endswith('.txt'))

# 找出没有对应图像的标签文件
labels_to_delete = label_files - image_files

# 删除没有对应图像的标签文件
for label in labels_to_delete:
    label_file_path = os.path.join(labels_path, label + '.txt')
    os.remove(label_file_path)
    print(f'Deleted: {label_file_path}')

print('Operation completed.')
