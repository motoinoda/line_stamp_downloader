# line_stamp_downloader
# 注意：「私的利用目的」で使用してください
# 注意：「ダウンロードした画像をアップロードした場合，著作権法違反になります」
## 機能
- line スタンプの url を貼ることでスタンプデータを一括でダウンロードできます.
- 画像は png，アニメーションは png(apng) と gif で保存されます．
- gif が保存されない場合は別ツールでapng -> gif に変換してください．


## 使い方(実行ファイルからダウンロードする場合[macのみ対応])
1. git からダウンロード
2. 自分の pc の cpu にあったファイルを選択（M1, M2, M3 は apple_silicon, intel cpu は intel_mac） 
3. apple_silicon, intel_mac の dist 内の実行ファイルを開く．（開かない場合は右クリックから開くを選択）
4. ターミナルが開き，"lineスタンプのURLを入力してください: " と出るまで待つ（数十秒程度かかる場合がある）
5. ほしい line スタンプのページの url を貼り付ける
6. 保存先のディレクトリを入力**
7. 指定したディレクトリにスタンプ画像がすべて保存される




**注意
- "./" は home になっている, デスクトップに保存する場合 "./Desktop/ファイル名/" とする
- 保存先のディレクトリがない場合自動で生成される

## pyファイルから実行する場合(windowsにも対応)
- pip でインストールできるライブラリのみを使用しているのでコード見ながら環境作って実行






##### その他
- ラインスタンプダウンロード
- lineスタンプダウンロード
- line sticker download，