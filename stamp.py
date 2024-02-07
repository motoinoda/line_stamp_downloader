import re
import imageio
import requests
import os
import sys
import click
from PIL import Image


def download_stickers(website_url, output_folder):
    response = requests.get(website_url)
    html_content = response.text

    pre = re.findall(r"data-preview='{(.*?)}'", html_content)
    if len(pre) == 0:
        print("URLが間違っています。")
        print("https://store.line.me/home/ja からほしいスタンプを選んでURLをコピーしてください。")
        return

    if not os.path.isdir(output_folder):
        os.makedirs(output_folder)

    type_dict = {'static': 'staticUrl', 'animation': 'animationUrl',
                 'animation_sound': 'animationUrl', 'popup': 'popupUrl', 'sound': 'staticUrl'}
    for k, input_text in enumerate(pre, start=1):
        pattern_type = r'&quot;([^&]*)&quot; :'
        pattern_body = r': &quot;([^&]*)&quot;'
        types = re.findall(pattern_type, input_text)
        body = re.findall(pattern_body, input_text)
        typedef = dict(zip(types,body))
        data_type = type_dict[typedef['type']]
        if data_type == 'staticUrl':
            url = typedef[data_type]
            img_name = os.path.basename(url)
            img_path = os.path.join(output_folder, str(k))
            download_image(url, img_path)
        else:
            url = typedef[data_type]
            img_name = os.path.basename(url)
            img_path = os.path.join(output_folder, str(k))
            download_image(url, img_path)
            convert_to_gif(img_path)
        print(k,"枚保存しました")


def download_image(url, img_path):
    with open(img_path + ".png", 'wb') as img_file:
        img_response = requests.get(url)
        img = img_response.content
        img_file.write(img)


def convert_to_gif(img_path):
    images = imageio.mimread(img_path + ".png")
    frames = []
    if images[0].shape[2] == 4:
        for frame in images:
            img = Image.fromarray(frame)
            frames.append(img)
        frames[0].save(img_path + ".gif", save_all=True, append_images=frames[1:], disposal=2, duration=100, loop=0)
    else:
        print("このAPNGはGIF化できませんでした。")
        print("APNGのみ保存されます。")
        print("別なツールでAPNGをGIFに変換してください。")


if __name__ == "__main__":
    website_url = click.prompt("LINEスタンプのURLを入力してください", type=str)
    output_folder = click.prompt("保存先のパスを入力してください。存在しない場合は自動で作成されます。./はhomeになります", type=str)
    download_stickers(website_url, output_folder)
