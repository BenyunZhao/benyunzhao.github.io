from PIL import Image

# 原始图片路径
input_path = "/Users/claude/Documents/GitHub/benyunzhao.github.io/images/maple.png"
# 输出文件名前缀
output_prefix = "/Users/claude/Documents/GitHub/benyunzhao.github.io/images/maple"

# 需要保存的尺寸
sizes = [512, 196, 32, 16]

# 打开原始图片
img = Image.open(input_path)

for size in sizes:
    # 缩放图片为正方形
    img_resized = img.resize((size, size), Image.LANCZOS)
    # 保存为 PNG 格式
    img_resized.save(f"{output_prefix}_{size}x{size}.png")

print("图片已保存为多种分辨率！")