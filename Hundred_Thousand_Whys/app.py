from flask import Flask
import config
from extension import db
from blueprint.QA import bp as qa_bp
from blueprint.authorize import bp as auth_bp
from models import UserModel
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


# HOSTNAME = '127.0.0.1'
# PORT = '3306'
# DATABASE = 'database'
# USERNAME = 'root'
# PASSWORD = 'longjiayu991216'
# DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
# app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
#
# db = SQLAlchemy(app)
#
# with db.engine.connect() as conn:
#     rs = conn.execute("select 1")
#     print(rs.fetchone())
app.config.from_object(config)  # connect to the file config.app

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
