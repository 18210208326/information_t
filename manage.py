# -*- coding: UTF-8 -*-
from flask import Flask
from config import Config
app = Flask(__name__)
#类的方式加载配制文件
app.config.from_object(Config)


@app.route("/")
def index():
    return 'ok test add 123'

@app.route("/")
def index1():
    return 'ok test add 123'
    
if __name__ == '__main__':
    app.run()
