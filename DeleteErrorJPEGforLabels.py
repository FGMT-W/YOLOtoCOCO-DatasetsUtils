import os


def check_and_delete_images(image_dir, label_dir):
    # 获取图片文件夹中的所有jpg图片文件
    image_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg')]

    # 初始化一个列表来存储没有对应标签的图片文件
    deleted_images = []

    for image_file in image_files:
        # 获取图片文件的基名（不带扩展名）
        base_name = os.path.splitext(image_file)[0]

        # 构造对应的标签文件名
        label_file = base_name + '.txt'

        # 检查标签文件是否存在
        if not os.path.exists(os.path.join(label_dir, label_file)):
            # 如果标签文件不存在，则删除图片文件
            os.remove(os.path.join(image_dir, image_file))
            # 将删除的图片文件名加入到列表中
            deleted_images.append(image_file)

    # 输出删除的图片文件列表
    print("Deleted images without corresponding label files:")
    for image in deleted_images:
        print(image)


# 使用示例
image_directory = 'C:/Users/thefr/Desktop/datasetsYOLOV3/images/val'
label_directory = 'C:/Users/thefr/Desktop/datasetsYOLOV3/labels/val'
check_and_delete_images(image_directory, label_directory)
