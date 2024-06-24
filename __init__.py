# app/__init__.py

from flask import Flask
from .models import db
from .routes.auth import auth_bp
from .routes.products import products_bp
from .routes.cart import cart_bp
from datetime import timedelta
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/ecomm_website'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    # app.config['SECRET_KEY'] = 'adgs5tywsfgs6ye8ik27uq9oks-yhqiknjwsyu29oalsmwo-p2w7yeravx'
    # app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=60) 
    app.config['JWT_SECRET_KEY'] = 'adgs5tywsfgs6ye8ik27uq9oks-yhqiknjwsyu29oalsmwo-p2w7yeravx'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=60)
    app.config['JWT_TOKEN_LOCATION'] = ['headers', 'cookies']


    db.init_app(app)

    jwt = JWTManager(app)

    jwt.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(cart_bp)

    return app
