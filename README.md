# Introduction
A simple example for pywebview.
# Install
```bash
pip install flask
pip install pywebview
```
# Usage
```bash
python app.py
```
# Build
```bash
sh package.sh
```
---
Note: 
- Windows
```bash
pyinstaller -w -F --add-data "templates;templates" --add-data "static;static" app.py
```
- Linux
```bash
pyinstaller -w -F --add-data "templates:templates" --add-data "static:static" app.py
```
# Issue
None.
# Reference
> [https://docs.python.org/3/library/webbrowser.html](https://docs.python.org/3/library/webbrowser.html)
> 
> [https://elc.github.io/posts/executable-flask-pyinstaller/](https://elc.github.io/posts/executable-flask-pyinstaller)
> 
> [https://stackoverflow.com/questions/32149892/flask-application-built-using-pyinstaller-not-rendering-index-html](https://stackoverflow.com/questions/32149892/flask-application-built-using-pyinstaller-not-rendering-index-html)
> 
> [https://github.com/ClimenteA/flaskwebgui](https://github.com/ClimenteA/flaskwebgui)
> 
> [https://github.com/Widdershin/flask-desktop](https://github.com/Widdershin/flask-desktop)
> Bootstrap 3D buttons: [https://codepen.io/bepctak/pen/ojXjzR](https://codepen.io/bepctak/pen/ojXjzR)