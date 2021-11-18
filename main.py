import datetime
from flask_login import LoginManager, UserMixin
from flask_migrate import Migrate
from flask import Flask, render_template, app, request
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask import jsonify
from flask import request
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from werkzeug.security import check_password_hash

app = Flask(__name__)

POSTGRES = {
    'user': 'postgres',
    'pw': '123',
    'db': 'site',
    'host': '127.0.0.1',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config["SECRET_KEY"] = "ich-lebe-diese"

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)


class ProductCategories(db.Model):
    __tablename__ = 'product_categories'

    pcid = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(500))
    products = db.relationship("Product", backref='product_categories')

    def __repr__(self):
        return f"{self.pcid}:{self.category}:{self.description}:{self.products}"


class Product(db.Model):
    __tablename__ = 'product'

    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), db.CheckConstraint('check>5'))
    description = db.Column(db.String(500))
    price = db.Column(db.Float, db.CheckConstraint('check>0'))
    amount = db.Column(db.Integer, db.CheckConstraint('check>0'))
    image = db.Column(db.LargeBinary)
    histories = db.relationship("History", backref='product')
    pcid = db.Column(db.Integer, db.ForeignKey('product_categories.pcid'))

    def __repr__(self):
        return f"{self.pid}:{self.name}:{self.description}:{self.price}:{self.amount}:{self.image}:{self.pcid}"


class History(db.Model):
    __tablename__ = 'history'

    id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.Integer, db.ForeignKey('product.pid'))
    date_of_change = db.Column(db.DateTime, onupdate=datetime.timezone.utc)
    old_amount = db.Column(db.Integer, db.CheckConstraint('check>0'))
    new_amount = db.Column(db.Integer, db.CheckConstraint('check>0'))

    def __repr__(self):
        return f"{self.id}:{self.date_of_change}:{self.old_amount}:{self.new_amount}:{self.pid}"


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    alternative_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"{self.id}:{self.email}:{self.password}:{self.registered_on}:{self.admin}"


@app.route('/categories', methods=['POST', 'GET'])
def handle_categories():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_category = ProductCategories(category=data["category"], description=data["description"])
            db.session.add(new_category)
            db.session.commit()
            return {"message": f"category {new_category.category} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        categories = ProductCategories.query.all()
        results = [
            {
                "category": categories.category,
                "description": categories.description,
            } for categories in categories]

        return {"count": len(results), "categories": results}


@app.route('/categories/', methods=['PUT', 'DELETE'])
def handle_category(product_categories_pcid):
    category = ProductCategories.query.get(product_categories_pcid)

    if request.method == 'PUT':
        data = request.get_json()
        category.category = data['category']
        category.description = data['description']
        db.session.add(category)
        db.session.commit()
        return {"message": f"category {category.category} successfully updated"}

    elif request.method == 'DELETE':
        db.session.delete(category)
        db.session.commit()
        return {"message": f"category {category.category} successfully deleted."}


@app.route('/products', methods=['POST', 'GET'])
def handle_products():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_product = Product(name=data['name'], description=data['description'],
                                  price=data['price'], amount=data['amount'], image=['image'], pcid=['pcid'])
            db.session.add(new_product)
            db.session.commit()
            return {"message": f"product {new_product.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        products = Product.query.all()
        results = [
            {
                "name": products.name,
                "description": products.description,
                "price": products.price,
                "amount": products.amount,
                "product_category": products.pcid,
                "image": products.image
            } for products in products]
        return {"products": results}


@app.route('/products/<int:product_pid>', methods=['GET', 'PUT', 'DELETE'])
def handle_product(product_pid):
    product = Product.query.get(product_pid)

    if request.method == 'PUT':
        data = request.get_json()
        product.pid = data['pid']
        product.name = data['name']
        product.description = data['description']
        product.price = data['price']
        product.amount = data['amount']
        product.pcid = data['pcid']
        product.image = data['image']
        db.session.add(product)
        db.session.add(product)
        db.session.commit()
        return {"message": f"product {product.name} successfully updated"}

    elif request.method == 'DELETE':
        db.session.delete(product)
        db.session.commit()
        return {"message": f"product {product.name} successfully deleted."}


if __name__ == "__main__":
    app.run(debug=True)
