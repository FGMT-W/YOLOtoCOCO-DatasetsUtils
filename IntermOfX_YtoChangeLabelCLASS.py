import os

# 数据集路径
dataset_path = 'C:/Users/thefr/Desktop/绿光-白天5m/'
# 标签文件夹路径
labels_path = os.path.join(dataset_path, 'labels')

# 设置要替换的文件范围
start_frame = 22578
end_frame = 22611

# 设置要替换的标签类别
old_label = '8'
new_label = '9'

# 遍历文件范围内的标签文件
for frame_number in range(start_frame, end_frame + 1):
    label_file_name = f'frame_{frame_number}.txt'
    label_file_path = os.path.join(labels_path, label_file_name)

    if os.path.exists(label_file_path):
        with open(label_file_path, 'r') as file:
            lines = file.readlines()

        with open(label_file_path, 'w') as file:
            for line in lines:
                # 替换标签类别
                parts = line.split()
                if parts[0] == old_label:
                    parts[0] = new_label
                new_line = ' '.join(parts)
                file.write(new_line + '\n')

        print(f'Updated: {label_file_path}')
    else:
        print(f'File not found: {label_file_path}')

print('Operation completed.')
