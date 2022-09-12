import datetime
import glob
import os
import shutil
from PIL import Image, ImageOps

dt_now = datetime.datetime.now()
timestamp = dt_now.strftime('%Y%m%d%H%M%S')
check_dir_path = "./image/checked/" + timestamp

print("処理開始")

# 退避用ディレクトリ作成
os.mkdir(check_dir_path)

images = glob.glob("./image/input/*.png")
for image_path in images:
    print(image_path)

    image_file_name = os.path.split(image_path)[1]

    # 画像の加工 今回は説明の為、簡略化（invert加工のみ）
    image = Image.open(image_path).convert('RGB')
    image_invert = ImageOps.invert(image)
    image_invert.save("./image/output/" + image_file_name + "_invert.png")

    print("画像変換完了：" + image_file_name)

    # 処理済みファイルの退避
    shutil.copy2(image_path, check_dir_path + "/" + image_file_name)
    print("画像退避完了：" + image_file_name)

    # 処理済みファイルを削除
    os.remove(image_path)
    print("画像削除完了：" + image_file_name)

print("処理完了")
