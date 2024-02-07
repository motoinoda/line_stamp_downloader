# line_stamp_downloader
# 「私的利用目的」でのみ使用してください
## 機能
- lineのスタンプのurlを貼ればスタンプデータをダウンロードできます.
- 画像はpng，アニメーションはpng(apng)とgifで保存されます．
- gifが保存されない場合は別ツールでapng -> gif に変換してください．


## 使い方(実行ファイルからダウンロードする場合[macのみ対応])
1. git からダウンロード
2. 自分の pc の cpu にあったファイルを選択（M1, M2, M3 は apple_silicon, intel cpu は intel_mac） 
3. apple_silicon, intel_mac の dist 内の実行ファイルを開く．（開かない場合は右クリックから開くを選択）
4. ターミナルが開き，"lineスタンプのURLを入力してください: " と出るまで待つ（数十秒程度かかる場合がある）
5. ほしい line スタンプのページの url を貼り付ける
6. 保存先のディレクトリを入力**
7. 指定したディレクトリにスタンプ画像がすべて保存される




**注意
- "./" は home になっている, デスクトップに保存する場合 "./Desktop/ファイル名/"とする
- 保存先のディレクトリがない場合自動で生成される

## .pyから実行する場合(windowsにも対応)
- pipでインストールできるライブラリのみを使用しているのでコード見ながら環境作って実行