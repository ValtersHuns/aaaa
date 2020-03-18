from flask import Flask
from models import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://qxjnzonbylcpsu:5345f4eaa942791f5b2b718eef3414b1b58177637e3b52c1b205b5ed876c0c0d@ec2-54-195-247-108.eu-west-1.compute.amazonaws.com:5432/d5qem9lmnv7j9b'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
