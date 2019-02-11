# -*- coding: UTF-8 -*-
from flask import Flask
from config import Config
app = Flask(__name__)
#类的方式加载配制文件
app.config.from_object(Config)
def test():
return 'ok'

@app.route("/")
def index():
    return 'ok test add 123'


def admin
 
 print(####)
if __name__ == '__main__':
    app.run()
