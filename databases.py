from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()



def add_product(name, price, picture_link, description):
    product_object = product(
        name=name,
        price=price,
        picture_link = picture_link,
        description = description
        )
    session.add(product)
    session.commit()

def query_product_by_id(id_number):
	Product = session.query(Product).filter_by(
		id_number=id_number).first()
	return Customer


def delete_product_id(id_number):
	session.query(product).filter_by(
		id_number=id_number).delete()
	session.commit()


    
def query_all_products():
	product = session.query(product).all()
	return product

def edit_product_by_id(id,name,price,picture_link,description):
    product=session.query(product).filter_by(id_number=id_number).one()
    product.name=name
    product.price=price
    product.picture_link
    product.description=description
    session.commit()



def add_to_cart(productID):
    product1 = Cart(productID)
    session.add(product1)
    session.commit()






    
