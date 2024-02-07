import re
import imageio
from PIL import Image
import numpy as np
import requests
import os
import sys
import click


# args = sys.argv
# print("ディレクトリが存在しない場合自動で作成されます")
# if(len(args)!=3):
#     print("error")
#     print("実行する際の引数は以下のようにしてください")
#     print("python stamp.py save_dir line_url")
#     sys.exit()
# else:
#     output_folder=args[1]
#     website_url=args[2]


website_url = click.prompt("lineスタンプのURLを入力してください", type=str)

# ディレクトリパスを入力

output_folder = click.prompt("保存先のパスを入力してください，存在しない場合自動で作成されます，./はhomeになります", type=str)


# output_folder="./data"

##ほしいスタンプのurl(line公式)
#動画
# website_url = "https://store.line.me/stickershop/product/25533563/ja"
#画像
# website_url="https://store.line.me/stickershop/product/30130/ja"
response = requests.get(website_url)
html_content = response.text


##動くスタンプをダウンロードしたい時

# iphone_check=re.findall('iPhone',html_content)
https_urls_p = re.findall(r"https://stickershop.line-scdn.net/stickershop\S*android\S*",html_content)
https_urls_a = re.findall(r"https://stickershop.line-scdn.net/stickershop\S*iPhone\S*",html_content)

if(len(https_urls_p)>len(https_urls_a)):
    print("画像のスタンプです")
    https_urls = re.findall(r"https://stickershop.line-scdn.net/stickershop\S*android\S*",html_content)
    
    # 抽出したURLを出力
    for i, url in enumerate(https_urls):
        # anime_url=re.findall("\S+animation\S+",url)
        # print(url)

        if(i%4==0):
            url=url[:-11]
            print(url)
            # 画像をダウンロードして保存
            #ディレクトりなければ作る
            if not os.path.isdir(output_folder):
                os.makedirs(output_folder)
            img_name = os.path.basename(url)
            img_path = os.path.join(output_folder, str(i))
            with open(img_path+".png", 'wb') as img_file:
                img_response = requests.get(url)
                # print(img_response.content)
                img=img_response.content
                # print(type(img))
                img_file.write(img)





else:
    print("動画のスタンプです")
    https_urls = re.findall(r"https://stickershop.line-scdn.net/stickershop\S*animation\S*",html_content)
   
    # 抽出したURLを出力
    for i, url in enumerate(https_urls):
        # anime_url=re.findall("\S+animation\S+",url)
        # print(url)
        url=url[:-11]
        print(url)

        #ディレクトりなければ作る
        if not os.path.isdir(output_folder):
            os.makedirs(output_folder)

        img_name = os.path.basename(url)
        img_path = os.path.join(output_folder, str(i))
        with open(img_path+".png", 'wb') as img_file:
            img_response = requests.get(url)
            # print(img_response.content)
            img=img_response.content
            # print(type(img))
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




