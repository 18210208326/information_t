#coding:utf8
import logging

#基本配置信息
class Config(object):

    DEBUG = True
    SECRET_KEY = "123456"

    #数据库配置
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:mysql@127.0.0.1:3306/information"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True #数据库内容发送改变之后,自动提交
    #SQLALCHEMY_ECHO=True
