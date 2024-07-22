import os

def count_labels_in_yolo(labels_path, num_labels=16):
    label_counts = [0] * num_labels  # 初始化标签计数列表

    # 获取所有txt文件名
    label_files = [f for f in os.listdir(labels_path) if f.endswith('.txt')]

    for label_file in label_files:
        with open(os.path.join(labels_path, label_file), 'r') as file:
            lines = file.readlines()
            for line in lines:
                label = int(line.split()[0])  # 假设标签在每行的第一列
                if 0 <= label < num_labels:
                    label_counts[label] += 1

    return label_counts

# 使用示例
labels_path = 'C:\\Users\\thefr\\Desktop\\datasetsYOLOV1\\labels\\val'

label_counts = count_labels_in_yolo(labels_path)
for label, count in enumerate(label_counts):
    print(f"标签 {label} 出现了 {count} 次")
