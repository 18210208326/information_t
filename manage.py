from flask import Flask
from config import Config
from modules.admin.admin import admin_blue
app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(admin_blue,url_prefix='/admin')
@app.route("/")
def test():
    return 'ok'

if __name__ == '__main__':
    app.run()