import os


def rename_images(folder_path, prefix="frame_", start_number=36900):
    # 获取指定文件夹中所有的jpg文件
    jpg_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]

    # 排序文件名，确保重命名时顺序一致
    jpg_files.sort()

    # 重命名文件
    for i, filename in enumerate(jpg_files):
        new_name = f"{prefix}{start_number + i}.jpg"
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, new_name)
        os.rename(src, dst)
        print(f'Renamed {src} to {dst}')


# 使用示例
folder_path = 'C:/Users/thefr/Desktop/datas'  # 替换为YOLO文件夹的实际路径
prefix = 'frame_'  # 可根据需求修改前缀
start_number = 36900  # 可根据需求设置起始数字
rename_images(folder_path, prefix, start_number)
