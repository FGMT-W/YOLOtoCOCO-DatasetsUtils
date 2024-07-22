import json
from collections import defaultdict


def check_coco_categories(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as f:
        coco_data = json.load(f)

    category_count = defaultdict(int)

    for annotation in coco_data['annotations']:
        category_id = annotation['category_id']
        category_count[category_id] += 1

    print("类别种类及序号:")
    for category_id, count in category_count.items():
        print(f"类别ID: {category_id}, 数量: {count}")


# 使用示例，替换为你的COCO JSON文件路径
json_file_path = 'C:/Users/thefr/Desktop/datasetsCOCOV3/annotations/val_instances.json'
check_coco_categories(json_file_path)