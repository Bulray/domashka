from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    with app.app_context():

        from app import routes
        db.create_all()
        from app import process
        process.migrate_user_roles(app.config['USER_ROLES_FIXTURE_PATH'])
        process.migrate_users(app.config['USERS_FIXTURE_PATH'])
        process.migrate_orders(app.config['ORDERS_FIXTURE_PATH'])
        process.migrate_offers(app.config['OFFERS_FIXTURE_PATH'])
        return app
