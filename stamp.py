import re
import imageio
from PIL import Image
import numpy as np
import requests
import os
import sys
import click





website_url = click.prompt("lineスタンプのURLを入力してください", type=str)

output_folder = click.prompt("保存先のパスを入力してください，存在しない場合自動で作成されます，./はhomeになります", type=str)

response = requests.get(website_url)
html_content = response.text




pre = re.findall(r"data-preview='{(.*?)}'",html_content)
if(len(pre)==0):
    print("urlが間違っています")
    print("https://store.line.me/home/ja")
    print("からほしいスタンプを選んでurlをコピーしてください")
    sys.exit()

if not os.path.isdir(output_folder):
    os.makedirs(output_folder)

type_dict={'static':'staticUrl','animation':'animationUrl','animation_sound':'animationUrl','popup':'popupUrl','sound':'staticUrl'}
for k in range(1,len(pre)):
    input_text=pre[k]
    # print(pre)
    pattern_type = r'&quot;([^&]*)&quot; :'
    pattern_body = r': &quot;([^&]*)&quot;'
    types = re.findall(pattern_type, input_text)
    body = re.findall(pattern_body, input_text)
    typedef = dict(zip(types,body))
    data_type = type_dict[typedef['type']]
    url = typedef[data_type]
    if(data_type=='staticUrl'):
        img_name = os.path.basename(url)
        img_path = os.path.join(output_folder, str(k))
        with open(img_path+".png", 'wb') as img_file:
            img_response = requests.get(url)
            img=img_response.content
            img_file.write(img)

    else:
        img_name = os.path.basename(url)
        img_path = os.path.join(output_folder, str(k))
        with open(img_path+".png", 'wb') as img_file:
            img_response = requests.get(url)
            img=img_response.content
            img_file.write(img)

        images = imageio.mimread(img_path+".png")
        frames = []
        if(images[0].shape[2]==4):
            for i, frame in enumerate(images):
                img = Image.fromarray(frame)
                frames.append(img)
                frames[0].save(img_path+".gif", save_all=True, append_images=frames[1:],disposal=2 ,duration=100, loop=0)
        else:
            print("このapngはgif化できませんでした")
            print("apngのみ保存されます")
            print("別なツールでapngをgifに変換してください")
    print(k,"枚保存しました")

