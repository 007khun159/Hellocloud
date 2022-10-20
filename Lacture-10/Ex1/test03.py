from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
#Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Init db
db = SQLAlchemy(app)
#Init ma
ma = Marshmallow(app)

#Product Class/Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description  = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def init(self, name, description, price, qty ):
        self.name = name
        self.description = description
        self.price = price
        self.qty =qty

#Product Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')

#Init Schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
db.create_all()
#Run Server
if __name__ == 'main':
    app.run(debug=True)
