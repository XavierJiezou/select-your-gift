from flask import Flask, jsonify, request, render_template
import os
import sys
import webview


if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(
        __name__,
        template_folder=template_folder,
        static_folder=static_folder
    )
else:
    app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/add', methods=['POST'])
def add():
    a = request.values.get('a')
    b = request.values.get('b')
    c = float(a)+float(b)
    return jsonify({'c': c})


if __name__ == '__main__':
    webview.create_window('Flask example', app)
    webview.start()
