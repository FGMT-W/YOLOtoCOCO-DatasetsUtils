import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
image_path = 'utils/frame_1816.jpg'
image = cv2.imread(image_path)

# 检查图像是否成功读取
if image is None:
    print("Error: Unable to read the image. Please check the file path.")
else:
    # 转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 高斯滤波器
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 二值化处理
    _, binary = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)

    # 找到轮廓
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 找到最大轮廓
    largest_contours = sorted(contours, key=cv2.contourArea, reverse=True)[:2]

    # 绘制最大轮廓
    output_image = image.copy()
    cv2.drawContours(output_image, largest_contours, -1, (0, 255, 0), 2)

    # 创建蒙版并提取光斑区域
    mask = np.zeros_like(gray)
    cv2.drawContours(mask, largest_contours, -1, 255, thickness=cv2.FILLED)
    bright_spots = cv2.bitwise_and(image, image, mask=mask)

    # 计算光谱分析
    spectra = []
    for contour in largest_contours:
        mask_single = np.zeros_like(gray)
        cv2.drawContours(mask_single, [contour], -1, 255, thickness=cv2.FILLED)
        spot = cv2.bitwise_and(image, image, mask=mask_single)
        spectra.append(spot)

    # 显示结果
    plt.figure(figsize=(15, 10))

    plt.subplot(2, 3, 1)
    plt.title('Original Image')
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    plt.subplot(2, 3, 2)
    plt.title('Grayscale Image')
    plt.imshow(gray, cmap='gray')

    plt.subplot(2, 3, 3)
    plt.title('Blurred Image')
    plt.imshow(blurred, cmap='gray')

    plt.subplot(2, 3, 4)
    plt.title('Binary Image')
    plt.imshow(binary, cmap='gray')

    plt.subplot(2, 3, 5)
    plt.title('Largest Contours')
    plt.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))

    plt.subplot(2, 3, 6)
    plt.title('Bright Spots - Filtered and Contours')
    plt.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
    plt.imshow(bright_spots, alpha=0.5, cmap='hot')

    # 光谱分析可视化
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    for i, spot in enumerate(spectra):
        color = ('b', 'g', 'r')
        for j, col in enumerate(color):
            hist = cv2.calcHist([spot], [j], None, [256], [0, 256])
            axes[i].plot(hist, color=col)
        axes[i].set_xlim([0, 256])
        axes[i].set_title(f'Spectrum Analysis of Spot {i+1}')

    plt.tight_layout()
    plt.show()