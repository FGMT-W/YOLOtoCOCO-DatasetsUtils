import os

# 删除多余的重复标签，一个类在每个txt只保留第一次标记
def remove_duplicate_labels(image_dir, label_dir):
    # 获取图片和标签文件列表
    image_files = set(f[:-4] for f in os.listdir(image_dir) if f.endswith('.jpg'))
    label_files = set(f[:-4] for f in os.listdir(label_dir) if f.endswith('.txt'))

    # 找到所有有对应图片的标签文件
    common_files = image_files & label_files

    # 检查并移除重复标签
    for file in common_files:
        label_path = os.path.join(label_dir, f"{file}.txt")

        with open(label_path, 'r') as f:
            lines = f.readlines()

        label_counts = {}
        unique_lines = []

        for line in lines:
            label = line.split()[0]
            if label not in label_counts:
                label_counts[label] = 1
                unique_lines.append(line)
            elif label_counts[label] == 1:
                label_counts[label] += 1

        with open(label_path, 'w') as f:
            for line in unique_lines:
                f.write(line)

    print("重复标签删除完成")


# 设置图片和标签文件夹路径
image_directory = 'C:/Users/thefr/Desktop/绿光-白天20m/images'
label_directory = 'C:/Users/thefr/Desktop/绿光-白天20m/labels'

# 调用函数
remove_duplicate_labels(image_directory, label_directory)
