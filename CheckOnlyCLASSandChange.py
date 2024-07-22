import os

# 数据集路径
dataset_path = 'C:/Users/thefr/Desktop/datasets'
# 标签文件夹路径
labels_path = os.path.join(dataset_path, 'labels')

# 设置要替换的标签类别
old_label = '2'
new_label = '7'

# 遍历标签文件夹中的所有标签文件
for label_file_name in os.listdir(labels_path):
    label_file_path = os.path.join(labels_path, label_file_name)

    if label_file_name.endswith('.txt'):
        with open(label_file_path, 'r') as file:
            lines = file.readlines()

        # 检查文件中是否仅存在类别2的标注
        only_old_label = all(line.split()[0] == old_label for line in lines)

        if only_old_label:
            with open(label_file_path, 'w') as file:
                for line in lines:
                    parts = line.split()
                    parts[0] = new_label
                    new_line = ' '.join(parts)
                    file.write(new_line + '\n')

            print(f'Updated: {label_file_path}')
        else:
            print(f'Skipped (other labels present): {label_file_path}')

print('Operation completed.')
