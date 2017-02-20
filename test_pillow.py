from PIL import Image, ImageDraw

import random


def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 240 x 60:
width = 1280
height = 720
image = Image.new('RGB', (width, height), (255, 255, 255))

# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())

image.save('code.jpg', 'jpeg')
