from app import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from datetime import datetime


class UserRole(db.Model):
    __tablename__ = 'user_roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), primary_key=True)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, db.ForeignKey('user_roles.id'))
    phone = db.Column(db.String(16), unique=True)
    role = relationship('UserRole')
    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'email': self.email,
            'role':self.role.name,
            'phone': self.phone,

        }



class Offer(db.Model):
    __tablename__ = 'offers'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    executer_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    executer = relationship('User')
    Order = relationship('Order')


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    address = db.Column(db.String)
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    customer = relationship('User', foreign_keys='Order.customer_id')
    executor = relationship('User', foreign_keys='Order.executor_id')
    def serialize(self):
        return {
        'id': self.id,
        'name': self.name,
        'description': self.description,
        'start_date': self.start_date.isoformat(),
        'end_date': self.end_date.isoformat(),
        'address': self.address,
        'price': self.price,
        'customer_id': self.customer.customer_id(),
        'executor_id': self.executor.executor_id(),
        }

class Offer(db.Model):
    __tablename__ = 'offers'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    executer_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    executer = relationship('User')
    Order = relationship('Order')


    def serialize(self):
        return {
            'id': self.id,
            'order_id':  self.order_id,
            'executor_id': self.executor_id
        }

