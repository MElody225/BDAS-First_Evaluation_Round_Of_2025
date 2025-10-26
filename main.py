# main.py
from filters import grayscale, invert, warm, cool, oil_painting, anime_style
from utils import download_image
from PIL import Image
import os


def apply_filters(img, output_dir="output"):
    os.makedirs(output_dir, exist_ok=True)
    filters = {
        "grayscale": grayscale,
        "invert": invert,
        "warm": warm,
        "cool": cool,
        "oil_painting": oil_painting,
        "anime_style": anime_style
    }

    for name, func in filters.items():
        print(f"🎨 Applying filter: {name}")
        try:
            result = func(img)
            result.save(os.path.join(output_dir, f"{name}.png"))
        except Exception as e:
            print(f"❌ {name} failed: {e}")


if __name__ == "__main__":
    image_url = "https://cdn.pixabay.com/photo/2014/10/07/13/48/mountain-477832_1280.jpg"
    save_path = "images/input.jpg"

    download_image(image_url, save_path)
    img = Image.open(save_path).convert("RGB")

    apply_filters(img)
    print("✅ 所有滤镜已处理并保存到 output/ 目录")
