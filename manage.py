# -*- coding: UTF-8 -*-
from flask import Flask
from config import Config
app = Flask(__name__)
#类的方式加载配制文件
app.config.from_object(Config)


@app.route("/")
def index():
    return 'ok test add 123'

@app.route("/test")
def test():
	return 'test ok wsw'


def test2():
	return 'test2'

def test4():
	return 'test4'
if __name__ == '__main__':
    app.run()
