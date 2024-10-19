from flask import Flask, render_template,request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)


# アップロードされた画像を保存するディレクトリ
UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 許可されるファイルの拡張子を定義
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# ファイルの拡張子が許可されているか確認する関数
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# /homeにアクセスしたときにindex.htmlを表示
@app.route('/home')
def home():
    return render_template('sample1.html')
@app.route('/folium')
def folium1():
    return render_template('folium_test.html')
@app.route('/sendimg')
def recv_img():
    return render_template('sendimg.html')

# 画像ファイルをアップロードする処理
@app.route('/upload', methods=['POST'])
def upload_file():
    # リクエストにファイルが含まれているか確認
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']

    # 許可された拡張子であれば保存
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)  # ファイル名の安全性を確保
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))  # ファイルを保存
        return f'File {filename} uploaded successfully'

    return 'Invalid file type', 400
if __name__ == '__main__':
    app.run(debug=True)
