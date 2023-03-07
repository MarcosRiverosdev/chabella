from chabella.config.mysqlconnection import connectToMySQL
from flask import flash


class Product:
    def __init__(self,data) :
        self.id=data['id']
        self.name=data['name']
        self.description=data['description']
        self.id_category=data['id_category']
        self.image=data['image']
        self.price=data['price']
        self.existence=data['existence']
        self.likes=data['likes']
        self.sold=data['sold']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_all_products(cls):
        query="select * from products"
        results=connectToMySQL('chabella').query_db(query)
        productos=[]
        for valor in results:
            productos.append(cls(valor))
        return productos

    @classmethod
    def get_one_product(cls,data):
        query="select * from products inner join categories on categories.id=products.id_category where products.id=%(id)s"
        result=connectToMySQL('chabella').query_db(query,data)
        return result [0]

    @classmethod
    def save_product(cls,data):
        query="insert into products (name,description,id_category,image,price,existence,likes,sold, created_at, updated_at) values (%(name)s,%(description)s,%(id_category)s,%(image)s,%(price)s,0,0,0,now(),now());"
        result=connectToMySQL('chabella').query_db(query,data)
        return result

    @classmethod
    def destroy(cls,data):
        query="delete from products where id=%(id)s;"
        result=connectToMySQL('chabella').query_db(query,data)
        return result

    @classmethod
    def update_product(cls,data):
        query="update products set name=%(name)s,description=%(description)s,id_category=%(id_category)s,image=%(image)s,price=%(price)s, updated_at=now() where id=%(id)s;"
        result=connectToMySQL('chabella').query_db(query,data)
        return result

    @staticmethod
    def validate_register(product):
        is_valid=True
        query="select * from products where name=%(name)s"
        result=connectToMySQL('chabella').query_db(query,product)
        if  len(result)>=1:
            flash('Ya existe un producto registrado con ese nombre','product_filter')
            is_valid=False
        if len(product['name'])<1:
            flash('Debe completar el campo nombre','product_filter')
            is_valid=False
        if len(product['description'])<3:
            flash('Debe completar el campo descripcion','product_filter')
            is_valid=False
        if len(product['price'])<3:
            flash('Debe completar el campo precio','product_filter')
            is_valid=False
        if len(product['image'])<3:
            flash('Debe cargar la imagen de muestra','product_filter')
            is_valid=False
        return is_valid

    @classmethod
    def get_one_category(cls,data):
        query="select * from products inner join categories on products.id_category=categories.id where category=%(category)s"
        results=connectToMySQL('chabella').query_db(query,data)
        category=[]
        for valor in results:
            category.append(cls(valor))
        return category


class Most_Sold:
    def __init__(self,data) :
        self.id=data['id']
        self.image=data['image']
        self.sold=data['sold']
    
    @classmethod
    def get_most_vent(cls):
        query  = "select * from products order by sold desc limit 4;"
        result = connectToMySQL('chabella').query_db(query)
        sold=[]
        
        for valor in result:
            sold.append(cls(valor))
        return sold