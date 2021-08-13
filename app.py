from flask import Flask, jsonify, request, render_template
import os
import sys
import time
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


if __name__ == '__main__':
    # webview.create_window('SelectYourGift', app.run(debug=True))
    # webview.start()
    app.run(debug=True)
