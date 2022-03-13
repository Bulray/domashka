import requests

from app import models, db
from flask import current_app as app, jsonify, abort
import json


@app.route('/users', methods=['GET'])
def get_users():

    users = db.session.query(models.User).all()
    return jsonify([user.serialize for user in users])


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = db.session.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        abort(404)
    return jsonify(user.serialize())


@app.route('/orders', methods=['GET'])
def get_orders():
    orders = db.session.query(models.Order).all()
    return jsonify([order.serialize for order in orders])


@app.route('/orders<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = db.session.query(models.Order).filter(models.Order.id == order_id).first()
    if order is None:
        abort(404)
    return jsonify(order.serialize())


@app.route('/offers', methods=['GET'])
def get_offers():
    offers = db.session.query(models.Offer).all()
    return jsonify([offer.serialize for offer in offers])


@app.route('/offers<int:offer_id>', methods=['GET'])
def get_offer(offer_id):
    offer = db.session.query(models.Offer).filter(models.Offer.id == offer_id).first()
    if offer is None:
        abort(404)
    return jsonify(offer.serialize())


@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    db.session.add(models.User(**data))
    db.session.commit()
    return {}


@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    db.session.add(models.User(**data))
    db.session.commit()
    return {}


@app.route('/users/<int:user_id>', methods=['PUT'])
def edit_user(user_id):
    data = request.json
    user = db.session.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        abort(404)

    db.session.query(models.User).filter(models.User.id == user_id).update(data)
    db.session.commit()


    return{}

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = db.session.query(models.User).filter(models.User.id == user_id).delete()
    print(result)

    db.session/commit()
    return {}
