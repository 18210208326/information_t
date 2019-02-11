# -*- coding: UTF-8 -*-
from flask import Blueprint
admin_blue = Blueprint("admin",__name__)

@admin_blue.route("/")
def index():
    return 'admin ok'