import json
import os
import shutil

import cv2

# info ，license，categories 结构初始化；
# 在train.json,val.json,test.json里面信息是一致的；

# info，license暂时用不到
info = {
    "year": 2024,
    "version": '3.0',
    "date_created": 2024-7-22
}

licenses = {
    "id": 1,
    "name": "Long and short distance underwater laser communication",
    "url": "null",
}

# 自己的标签类别，跟yolo的数据集类别要对应好；
categories = [
    {"id": 1, "name": 'Facula reflection', "supercategory": 'Interference light'},
    {"id": 2, "name": 'Light scattering', "supercategory": 'Interference light'},
    {"id": 3, "name": '3m Blue purple facula', "supercategory": 'Daytime blue purple facula'},
    {"id": 4, "name": '5m Blue purple facula', "supercategory": 'Daytime blue purple facula'},
    {"id": 5, "name": '10m Blue purple facula', "supercategory": 'Daytime blue purple facula'},
    {"id": 6, "name": '15m Blue purple facula', "supercategory": 'Daytime blue purple facula'},
    {"id": 7, "name": '20m Blue purple facula', "supercategory": 'Daytime blue purple facula'},
    {"id": 8, "name": '5m Dark conditions Blue purple facula', "supercategory": 'Night blue purple facula'},
    {"id": 9, "name": '3m Green facula', "supercategory": 'Daytime green facula'},
    {"id": 10, "name": '5m Green facula', "supercategory": 'Daytime green facula'},
    {"id": 11, "name": '10m Green facula', "supercategory": 'Daytime green facula'},
    {"id": 12, "name": '15m Green facula', "supercategory": 'Daytime green facula'},
    {"id": 13, "name": '20m Green facula', "supercategory": 'Daytime green facula'},
    {"id": 14, "name": '5m Dark conditions Green facula', "supercategory": 'Night green facula'},
    {"id": 15, "name": 'Soft noise', "supercategory": 'Interference light'}
]

# 初始化train,test、valid 数据字典
# info licenses categories 在train和test里面都是一致的；
train_data = {'info': info, 'licenses': licenses, 'categories': categories, 'images': [], 'annotations': []}
test_data = {'info': info, 'licenses': licenses, 'categories': categories, 'images': [], 'annotations': []}
valid_data = {'info': info, 'licenses': licenses, 'categories': categories, 'images': [], 'annotations': []}


# image_path 对应yolov8的图像路径，比如images/train；
# label_path 对应yolov8的label路径，比如labels/train 跟images要对应；
def yolo_covert_coco_format(image_path, label_path):
    images = []
    annotations = []
    for index, img_file in enumerate(os.listdir(image_path)):
        if img_file.endswith('.jpg'):
            image_info = {}
            img = cv2.imread(os.path.join(image_path, img_file))
            height, width, channel = img.shape
            image_info['id'] = index
            image_info['file_name'] = img_file
            image_info['width'], image_info['height'] = width, height
        else:
            continue
        if image_info != {}:
            images.append(image_info)
        # 处理label信息-------
        label_file = os.path.join(label_path, img_file.replace('.jpg', '.txt'))
        with open(label_file, 'r') as f:
            for idx, line in enumerate(f.readlines()):
                info_annotation = {}
                class_num, xs, ys, ws, hs = line.strip().split(' ')
                class_id, xc, yc, w, h = int(class_num), float(xs), float(ys), float(ws), float(hs)
                xmin = (xc - w / 2) * width
                ymin = (yc - h / 2) * height
                xmax = (xc + w / 2) * width
                ymax = (yc + h / 2) * height
                bbox_w = int(width * w)
                bbox_h = int(height * h)
                img_copy = img[int(ymin):int(ymax), int(xmin):int(xmax)].copy()

                info_annotation["category_id"] = class_id  # 类别的id
                info_annotation['bbox'] = [xmin, ymin, bbox_w, bbox_h]  ## bbox的坐标
                info_annotation['area'] = bbox_h * bbox_w  ###area
                info_annotation['image_id'] = index  # bbox的id
                info_annotation['id'] = index * 100 + idx  # bbox的id
                # cv2.imwrite(f"./temp/{info_annotation['id']}.jpg", img_copy)
                info_annotation['segmentation'] = [[xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax]]  # 四个点的坐标
                info_annotation['iscrowd'] = 0  # 单例
                annotations.append(info_annotation)
    return images, annotations


# key == train，test，val
# 对应要生成的json文件，比如instances_train.json，instances_test.json，instances_val.json
def gen_json_file(yolov8_data_path, coco_format_path, key):
    # json path
    json_path = os.path.join(coco_format_path, f'annotations/{key}_instances.json')
    dst_path = os.path.join(coco_format_path, f'{key}')
    if not os.path.exists(os.path.dirname(json_path)):
        os.makedirs(os.path.dirname(json_path), exist_ok=True)
    data_path = os.path.join(yolov8_data_path, f'images/{key}')
    label_path = os.path.join(yolov8_data_path, f'labels/{key}')
    images, anns = yolo_covert_coco_format(data_path, label_path)
    if key == 'train':
        train_data['images'] = images
        train_data['annotations'] = anns
        with open(json_path, 'w') as f:
            json.dump(train_data, f, indent=2)
        # shutil.copy(data_path,'')
    elif key == 'test':
        test_data['images'] = images
        test_data['annotations'] = anns
        with open(json_path, 'w') as f:
            json.dump(test_data, f, indent=2)
    elif key == 'val':
        valid_data['images'] = images
        valid_data['annotations'] = anns
        with open(json_path, 'w') as f:
            json.dump(valid_data, f, indent=2)
    else:
        print(f'key is {key}')
    print(f'generate {key} json success!')
    return


if __name__ == '__main__':
    yolov8_data_path = 'C:/Users/thefr/Desktop/datasetsYOLOV3'
    coco_format_path = 'C:/Users/thefr/Desktop/datasetsCOCOV3'
    gen_json_file(yolov8_data_path, coco_format_path, key='train')
    gen_json_file(yolov8_data_path, coco_format_path, key='val')
    gen_json_file(yolov8_data_path, coco_format_path, key='test')