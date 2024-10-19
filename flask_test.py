from flask import Flask, render_template

app = Flask(__name__)

# /homeにアクセスしたときにindex.htmlを表示
@app.route('/home')
def home():
    return render_template('sample1.html')
@app.route('/folium')
def folium1():
    return render_template('folium_test.html')

if __name__ == '__main__':
    app.run(debug=True)
