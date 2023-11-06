from app import db
from app.models import Category, Product


def getCategories():
    return db.session.query(Category).all()


def getProducts(kw):
    products = db.session.query(Product).all()
    if kw:
        products = db.session.query(Product).filter(Product.name.contains(kw)).all()

    return products
