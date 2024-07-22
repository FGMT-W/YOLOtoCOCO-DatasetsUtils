import os
from PIL import Image

def merge_images(image1_path, image2_path, output_path):
    # 打开两张图片
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # 获取第一张图片的尺寸
    width1, height1 = image1.size

    # 调整第二张图片的尺寸与第一张相同
    image2 = image2.resize((width1, height1))

    # 创建一个新的空白图片，尺寸为两张图片横向拼接后的尺寸
    merged_image = Image.new('RGB', (width1 * 2, height1))

    # 将两张图片拼接到新图片上
    merged_image.paste(image1, (0, 0))
    merged_image.paste(image2, (width1, 0))

    # 保存合成后的图片
    merged_image.save(output_path)

def merge_images_from_folders(folder1, folder2, output_folder):
    # 获取两个文件夹中的所有图片文件名
    images1 = sorted(os.listdir(folder1))
    images2 = sorted(os.listdir(folder2))

    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 逐对读取和拼接图片
    for idx, (image1_name, image2_name) in enumerate(zip(images1, images2), start=1592):
        image1_path = os.path.join(folder1, image1_name)
        image2_path = os.path.join(folder2, image2_name)
        output_path = os.path.join(output_folder, f"frame_{idx}.jpg")

        merge_images(image1_path, image2_path, output_path)

# 示例用法
folder1 = 'F:\MLproject\data\images3'
folder2 = 'F:\MLproject\data\imagest'
output_folder = 'F:\MLproject\data\images6_23PG'
merge_images_from_folders(folder1, folder2, output_folder)
