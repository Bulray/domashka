import os
import json
import re
from datetime import datetime
from app import db, models
from sqlalchemy.sql import exists

DATE_PATTERN = re.compile(r'\d{2}/\d{2}/\d{4}')


def load_fixture(file_path):
    '''
    загружает содержимое текстуры
    '''
    content = []
    if os.path.isfile(file_path):
        with open(file_path) as file:
            content = json.load(file)

    return content


def migrate_user_roles(fixture_path):
    fixture_content = load_fixture(fixture_path)
    for role in fixture_content:
        if db.session.query(models.UserRole).filter(models.UserRole.id == role['id']).first() is None:
            n_role = models.UserRole(**role)
            db.session.add(n_role)

    db.session.commit()


def migrate_users(fixture_path):
    fixture_content = load_fixture(fixture_path)
    for user in fixture_content:
        if db.session.query(models.User).filter(models.User.id == role['id']).first() is None:
            db.session.add(models.User(**user))
    db.session.commit()


def migrate_orders(fixture_path):
    fixture_content = load_fixture(fixture_path)
    for order in fixture_content:
        for field_name, field_value in fixture_content.items():
            if isinstance(field_value, str) and re.search(DATE_PATTERN, field_value):
                order[field_name] = datetime.strptime(field_value, '%d/%M/%Y').date()

        if db.session.query(models.Order).filter(models.Order.id == role['id']).first() is None:
            db.session.add(models.Order(**order))
    db.session.commit()


def migrate_offers(fixture_path):
    fixture_content = load_fixture(fixture_path)
    for offer in fixture_content:
        if db.session.query(models.Offer).filter(models.Offer.id == role['id']).first() is None:
            db.session.add(models.Offer(**Offer))
    db.session.commit()
