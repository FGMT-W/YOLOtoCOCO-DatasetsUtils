import os
from ultralytics import YOLO
import multiprocessing

if __name__ == '__main__':
    multiprocessing.freeze_support()

    # 指定文件夹路径
    folder_path = r"/home/leiez/yolov8/yolov8/datas/"
    # 指定保存结果的文件夹路径
    output_folder_path = r"/home/leiez/yolov8/yolov8/labels/"

    # 如果保存结果的文件夹不存在，则创建它
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    # 加载之前训练完的模型
    model = YOLO(r"/home/leiez/yolov8/yolov8/runs/detect/train_v88/weights/best.pt")

    # 遍历文件夹中的文件
    for filename in os.listdir(folder_path):
        # 判断文件是否为图片文件
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # 拼接文件的完整路径
            file_path = os.path.join(folder_path, filename)
            # 预测并生成标签
            results = model(file_path, save=True, save_dir=output_folder_path)