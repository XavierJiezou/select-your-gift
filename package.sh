pip install pipenv
pipenv install
pipenv shell
pip install flask
pip install pywebview
pip install pyinstaller
pyinstaller -w -F -i favicon.ico --add-data "templates;templates" --add-data "static;static" app.py
pipenv --rm
