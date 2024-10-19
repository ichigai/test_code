# ファイル探索、フルパス表示
import glob
import os

# カレントディレクトリ以下のファイルを再帰的に検索
for filepath in glob.glob('**/*', recursive=True):
    # ファイルかどうかを確認してからフルパスを表示
    if os.path.isfile(filepath):
        print(os.path.abspath(filepath))
