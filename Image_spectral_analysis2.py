import cv2
import numpy as np
import matplotlib.pyplot as plt


def color_segmentation(image):
    # 转换为HSV颜色空间
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 定义颜色范围
    color_ranges = {
        'blue_purple': ([120, 50, 50], [170, 255, 255]),
        'green': ([35, 50, 50], [85, 255, 255]),
        'white': ([0, 0, 200], [180, 50, 255]),
        'yellow': ([20, 50, 50], [35, 255, 255])
    }

    masks = {}
    for color, (lower, upper) in color_ranges.items():
        lower = np.array(lower)
        upper = np.array(upper)
        masks[color] = cv2.inRange(hsv, lower, upper)

    return masks


def filter_and_analyze(image, masks):
    filtered_results = {}
    for color, mask in masks.items():
        # 应用双边滤波
        filtered_image = cv2.bilateralFilter(image, 9, 75, 75)

        # 提取感兴趣区域
        result = cv2.bitwise_and(filtered_image, filtered_image, mask=mask)

        # 转换为灰度图
        gray_result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

        # 边缘检测
        edges = cv2.Canny(gray_result, 50, 150)

        # 查找轮廓
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        filtered_results[color] = {
            'image': result,
            'edges': edges,
            'contours': contours
        }

    return filtered_results


def visualize_results(image, filtered_results):
    plt.figure(figsize=(18, 12))

    plt.subplot(3, 3, 1)
    plt.title('Original Image')
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    i = 2
    for color, results in filtered_results.items():
        plt.subplot(3, 3, i)
        plt.title(f'{color.capitalize()} Light')
        plt.imshow(cv2.cvtColor(results['image'], cv2.COLOR_BGR2RGB))
        plt.axis('off')

        plt.subplot(3, 3, i + 1)
        plt.title(f'{color.capitalize()} Edges')
        plt.imshow(results['edges'], cmap='gray')
        plt.axis('off')

        i += 2

    plt.show()


# 示例使用
image_path = 'utils/frame_1816.jpg'
image = cv2.imread(image_path)

# 颜色分割
masks = color_segmentation(image)

# 滤波与特征提取
filtered_results = filter_and_analyze(image, masks)

# 可视化结果
visualize_results(image, filtered_results)
