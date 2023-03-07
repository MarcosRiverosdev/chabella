from chabella.config.mysqlconnection import connectToMySQL
from flask import flash

class Category:
    def __init__(self,data) :
        self.id=data['id']
        self.category=data['category']

    @classmethod
    def get_all_categories(cls):
        query="select * from categories"
        results=connectToMySQL('chabella').query_db(query)
        users=[]
        for valor in results:
            users.append(cls(valor))
        return users

    @classmethod
    def save_category(cls,data):
        query="insert into categories (category) values (%(category)s);"
        result=connectToMySQL('chabella').query_db(query,data)
        return result
    
    @staticmethod
    def validate_register(category):
        is_valid=True
        query="select * from categories where category=%(category)s"
        result=connectToMySQL('chabella').query_db(query,category)
        if  len(result)>=1:
            flash('Category already taken','cat')
            is_valid=False
        if len(category['category'])<1:
            flash('Debe ingresar el campo','cat')
            is_valid=False
        return is_valid