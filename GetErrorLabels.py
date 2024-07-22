import os

def check_yolo_files(images_path, labels_path):
    # 获取所有jpg和txt文件名
    image_files = [f for f in os.listdir(images_path) if f.endswith('.jpg')]
    label_files = [f for f in os.listdir(labels_path) if f.endswith('.txt')]

    # 去除扩展名，只保留文件名部分
    image_files_no_ext = [os.path.splitext(f)[0] for f in image_files]
    label_files_no_ext = [os.path.splitext(f)[0] for f in label_files]

    # 找出没有对应标签的图片文件
    unmatched_images = [f + '.jpg' for f in image_files_no_ext if f not in label_files_no_ext]

    return unmatched_images

# 使用示例
images_path = 'C:/Users/thefr/Desktop/AG_Result/images'
labels_path = 'C:/Users/thefr/Desktop/AG_Result/labels'

unmatched_images = check_yolo_files(images_path, labels_path)
if unmatched_images:
    print("以下JPG文件没有对应的标签文件：")
    for img in unmatched_images:
        print(img)
else:
    print("所有JPG文件都有对应的标签文件。")
