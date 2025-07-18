import os

IMAGE_DIR = "images"
OUTPUT_FILE = "images.md"

# md_lines = ["## 图片预览\n"]

for file in sorted(os.listdir(IMAGE_DIR)):
    if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp')):
        md_lines.append(f"![{file}]({IMAGE_DIR}/{file})")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))
