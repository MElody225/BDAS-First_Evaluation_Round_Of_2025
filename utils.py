import requests
import os
from PIL import Image
import matplotlib.pyplot as plt

def download_image(url, save_path):
    """从 URL 下载图片"""
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(response.content)
        print(f" √ 图片已下载: {save_path}")
    else:

        print(" × 下载失败:", response.status_code)
