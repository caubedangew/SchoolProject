from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app import app, db


class Category(db.Model):
    __tablename__ = "category"

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship("Product", backref='category', lazy=True)

class Product(db.Model):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    description = Column(String(50))
    image = Column(String(200))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

if __name__ == "__main__":
    with app.app_context():
        pass
        c1 = Category(name="Laptop")
        c2 = Category(name="Speaker")
        db.session.add(c1)
        db.session.add(c2)
        # p1 = Product(name="iPhone 7 Plus", description="Apple, 32GB, RAM: 3GB, iOS13", price=17000000, image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg", category_id=1)
        # p2 = Product(name="iPad Pro 2020", description="Apple, 128GB, RAM: 6GB", price=37000000, image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg", category_id=2)
        # p3 = Product(name="Galaxy Note 10 Plus", description="Samsung, 64GB, RAML: 6GB", price=24000000, image="https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg", category_id=1)
        # db.session.add_all([p1, p2, p3])
        db.session.commit()
        #db.create_all()

