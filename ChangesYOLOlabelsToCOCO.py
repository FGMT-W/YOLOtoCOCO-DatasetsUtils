import os

def update_yolo_labels(labels_dir):
    # 遍历标签文件目录
    for label_file in os.listdir(labels_dir):
        if label_file.endswith('.txt'):
            label_path = os.path.join(labels_dir, label_file)
            with open(label_path, 'r') as file:
                lines = file.readlines()

            # 标记是否存在格式不正确的标签
            has_format_error = False
            updated_lines = []

            # 更新类别ID
            for line in lines:
                parts = line.strip().split()
                if len(parts) == 5:  # 确保行包含5个值
                    class_id = int(parts[0])
                    # 类别ID +1
                    updated_class_id = class_id - 1
                    updated_line = ' '.join([str(updated_class_id)] + parts[1:])
                    updated_lines.append(updated_line)
                else:
                    print(f"Skipping line in {label_file} due to incorrect format: {line.strip()}")
                    has_format_error = True
                    break  # 一旦发现错误格式，跳出循环并删除文件

            if has_format_error:
                # 删除格式不正确的标签文件
                os.remove(label_path)
                print(f"Deleted file due to format errors: {label_file}")
            else:
                # 将更新后的标签写回文件
                with open(label_path, 'w') as file:
                    file.write('\n'.join(updated_lines) + '\n')

if __name__ == "__main__":
    # 标签文件所在目录
    labels_dir = 'C:\\Users\\thefr\\Desktop\\datasetsYOLOV3\\labels\\val'
    update_yolo_labels(labels_dir)
    print("标签文件更新完成")