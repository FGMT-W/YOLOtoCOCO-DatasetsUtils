import rasterio
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# 打开多光谱图像文件
with rasterio.open('utils/frame_1816.jpg', 'r') as dataset:
    # 读取所有波段数据
    multispectral_data = dataset.read()

# 将所有波段的图像尺寸调整为相同大小
resized_data = []
for band in multispectral_data:
    resized_band = np.array(Image.fromarray(band).resize((512, 512)))
    resized_data.append(resized_band)

# 将调整后的数据转换为numpy数组
resized_data = np.array(resized_data)

# 创建一个带有子图的画布
fig, axs = plt.subplots(len(resized_data), 1, figsize=(8, 3 * len(resized_data)))

# 在每个子图中显示波段图像
for i, band in enumerate(resized_data):
    axs[i].imshow(band, cmap='gray')
    axs[i].set_title(f'Band {i + 1}')
    axs[i].axis('off')

# 调整子图之间的间距
plt.tight_layout()

# 显示图像
plt.show()