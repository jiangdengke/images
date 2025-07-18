import os

IMAGE_DIR = "images"
README_FILE = "README.md"

intro_lines = [
    "## 图片预览\n"
]

image_lines = []

for file in sorted(os.listdir(IMAGE_DIR)):
    if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp')):
        image_lines.append(f"**{file}**")
        image_lines.append(f"![{file}]({IMAGE_DIR}/{file})\n")

with open(README_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(intro_lines + image_lines))
