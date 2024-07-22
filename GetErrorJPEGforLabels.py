import os

def find_missing_images(image_dir, label_dir):
    # 获取图片和标签文件列表
    image_files = set(f[:-4] for f in os.listdir(image_dir) if f.endswith('.jpg'))
    label_files = set(f[:-4] for f in os.listdir(label_dir) if f.endswith('.txt'))

    # 找出缺少对应图片的标签文件
    missing_images = label_files - image_files

    # 输出缺少的图片文件名
    if missing_images:
        print("以下标签文件没有对应的图片文件:")
        for missing_image in missing_images:
            print(f"{missing_image}.txt")
    else:
        print("所有标签文件都有对应的图片文件")

# 设置图片和标签文件夹路径
image_directory = 'C:/Users/thefr/Desktop/datasets/images'
label_directory = 'C:/Users/thefr/Desktop/datasets/labels'

# 调用函数
find_missing_images(image_directory, label_directory)
