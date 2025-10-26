from PIL import Image, ImageOps, ImageEnhance
import cv2
import numpy as np

def grayscale(img):
    return ImageOps.grayscale(img)

def invert(img):
    return ImageOps.invert(img)

def warm(img):
    enhancer = ImageEnhance.Color(img)
    return enhancer.enhance(1.5)

def cool(img):
    r, g, b = img.split()
    b = b.point(lambda i: i * 1.2)
    return Image.merge("RGB", (r, g, b))

# ========== 🎨 新增 AI 风格滤镜 ==========

def oil_painting(img):
    """油画风滤镜"""
    np_img = np.array(img)
    np_img = cv2.cvtColor(np_img, cv2.COLOR_RGB2BGR)
    dst = cv2.xphoto.oilPainting(np_img, 7, 1)
    dst = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
    return Image.fromarray(dst)

def anime_style(img):
    """动漫风滤镜"""
    np_img = np.array(img)
    np_img = cv2.cvtColor(np_img, cv2.COLOR_RGB2BGR)
    # 用双边滤波 & 边缘检测模拟卡通风格
    color = cv2.bilateralFilter(np_img, 9, 250, 250)
    gray = cv2.cvtColor(np_img, cv2.COLOR_BGR2GRAY)
    edges = cv2.adaptiveThreshold(cv2.medianBlur(gray, 7), 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 2)
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    cartoon = cv2.bitwise_and(color, edges)
    cartoon = cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB)
    return Image.fromarray(cartoon)
