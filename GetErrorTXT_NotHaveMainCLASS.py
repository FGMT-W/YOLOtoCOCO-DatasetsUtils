import os


def check_yolo_labels(images_dir, labels_dir, MainCLASS , NotMainCLASS):
    # 获取所有图片文件的文件名
    image_files = [f for f in os.listdir(images_dir) if f.endswith('.jpg')]

    # 用于存储只包含标签类别1而不包含标签类别3的标签文件名
    target_label_files = []

    for image_file in image_files:
        # 获取对应的标签文件名
        label_file = os.path.splitext(image_file)[0] + '.txt'
        label_path = os.path.join(labels_dir, label_file)

        if os.path.exists(label_path):
            with open(label_path, 'r') as f:
                labels = f.readlines()

            # 检查标签文件是否只包含类别MainCLASS且不包含类别NotMainCLASS
            contains_only_1 = all(int(label.split()[0]) == MainCLASS for label in labels)
            contains_3 = any(int(label.split()[0]) == NotMainCLASS for label in labels)

            if contains_only_1 and not contains_3:
                target_label_files.append(label_file)

    return target_label_files


# 示例用法
images_dir = 'C:/Users/thefr/Desktop/蓝光-白天5m/images'
labels_dir = 'C:/Users/thefr/Desktop/蓝光-白天5m/labels'
MainCLASS = 1
NotMainCLASS = 2
result_files = check_yolo_labels(images_dir, labels_dir, MainCLASS , NotMainCLASS)

print("只包含标签类别1而不包含标签类别3的标签文件有:")
for file in result_files:
    print(file)
