import os


def delete_classes_from_txt(file_path, classes_to_delete):
    """
    从txt文件中删除指定类别的信息
    参数：
        file_path: 文件路径
        classes_to_delete: 要删除的类别列表，例如 [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    返回：
        无
    """
    lines = []
    with open(file_path, 'r') as file:
        lines = file.readlines()

    updated_lines = []
    for line in lines:
        class_id, *rest = line.split(' ')
        class_id = int(class_id)
        if class_id not in classes_to_delete:
            updated_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(updated_lines)


def main():
    folder_path = "C:/Users/thefr/Desktop/绿光-白天20m/labels"  # 替换为实际的文件夹路径
    classes_to_delete = [0,1,2,3,4,5,6,7,8,9,10,11,13,14]

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            delete_classes_from_txt(file_path, classes_to_delete)

    print("指定类别信息已成功删除！")


if __name__ == "__main__":
    main()