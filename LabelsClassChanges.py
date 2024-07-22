import os


def modify_labels(folder_path):
    # 获取labels文件夹中所有的txt文件
    txt_files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]

    for txt_file in txt_files:
        with open(os.path.join(folder_path, txt_file), 'r') as f:
            lines = f.readlines()

        new_lines = [modify_line(line) for line in lines]

        # 覆盖原来的txt文件内容
        with open(os.path.join(folder_path, txt_file), 'w') as f:
            f.writelines(new_lines)


def modify_line(line):
    # 将类别X替换为类别Y
    class_id, *values = line.split()
    if class_id == '12':#X
        class_id = '14'#Y
    new_line = class_id + " " + " ".join(values) + "\n"
    return new_line


if __name__ == "__main__":
    dataset_labels_folder = "C:/Users/thefr/Desktop/datasets/labels"
    modify_labels(dataset_labels_folder)