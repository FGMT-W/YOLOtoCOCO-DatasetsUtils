import os


def check_and_delete_empty_labels(label_dir):
    # 获取标签文件目录下的所有文件名
    label_files = os.listdir(label_dir)

    # 用于存储被删除的文件名
    deleted_files = []

    for label_file in label_files:
        label_file_path = os.path.join(label_dir, label_file)

        # 检查文件内容
        with open(label_file_path, 'r') as f:
            lines = f.readlines()
            has_valid_class = False
            for line in lines:
                parts = line.strip().split()
                if parts and parts[0].isdigit():
                    class_id = int(parts[0])
                    if 0 <= class_id <= 14:
                        has_valid_class = True
                        break

            if not has_valid_class:
                # 删除没有类别0到14的文件
                os.remove(label_file_path)
                deleted_files.append(label_file_path)
                print(f"Deleted empty label file: {label_file_path}")

    return deleted_files


# 使用示例
label_directory = "C:/Users/thefr/Desktop/datasetsYOLOV2/labels/val"  # 替换为你的标签文件目录路径
deleted_files = check_and_delete_empty_labels(label_directory)
print(f"Total deleted files: {len(deleted_files)}")