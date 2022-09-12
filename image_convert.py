import datetime
from PIL import Image, ImageDraw

dt_now = datetime.datetime.now()
timestamp = dt_now.strftime('%Y%m%d%H%M%S')

base_image = Image.open('./lena.jpeg')
# 画像のフォーマット、サイズ、モードを取得
print(base_image.format, base_image.size, base_image.mode)


paste_image = Image.open('./order-big-tebura-3pack.png')
# 画像のフォーマット、サイズ、モードを取得
print(paste_image.format, paste_image.size, paste_image.mode)
paste_image.resize(base_image.size)
print(paste_image.format, paste_image.size, paste_image.mode)

# 貼り付け
paste_base_image = base_image.copy()
paste_base_image.paste(paste_image)
paste_base_image.save('./output/lena_3pack_' + timestamp + '.png')
