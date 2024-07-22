import os

def convert_label(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) > 0:
            # 将类别部分从小数改为整数
            parts[0] = str(int(float(parts[0])))
            new_lines.append(' '.join(parts))

    with open(file_path, 'w') as file:
        for line in new_lines:
            file.write(line + '\n')


def process_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                convert_label(file_path)
                print(f"Processed {file_path}")


# 设置你的YOLO标签文件的目录路径
directory_path = 'C:/Users/thefr/Desktop/datasetsYOLOV3/labels/val'
process_directory(directory_path)
