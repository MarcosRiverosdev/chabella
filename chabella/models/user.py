from chabella.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

class User:
    def __init__(self,data) :
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_all_users(cls):
        query="select * from user"
        results=connectToMySQL('chabella').query_db(query)
        users=[]
        for valor in results:
            users.append(cls(valor))
        return users

    @classmethod
    def save_user(cls,data):
        query="insert into user (first_name,last_name,email,password, created_at, updated_at) values (%(first_name)s,%(last_name)s,%(email)s,%(password)s,now(),now());"
        result=connectToMySQL('chabella').query_db(query,data)
        return result

    @classmethod
    def get_id(cls,data):
        query  = "select * from user where id = %(id)s;"
        result = connectToMySQL('chabella').query_db(query,data)
        return cls(result[0])

    @classmethod
    def get_one_user(cls,data):
        query  = "select * from user where id = %(id)s;"
        result = connectToMySQL('chabella').query_db(query,data)
        user=[]
        print(result)
        for valor in result:
            user.append(cls(valor))
        return cls(user)

    @classmethod
    def get_email(cls,data):
        query="select * from user where email=%(email)s"
        results=connectToMySQL('chabella').query_db(query,data)
        if len(results)<1:
            return False
        return cls(results[0])

    @classmethod
    def destroy(cls,data):
        query  = "delete from user where id = %(id)s;"
        return connectToMySQL('chabella').query_db(query,data)
    
    @classmethod
    def get_one(cls,data):
        query  = "select * from user where id = %(id)s;"
        result = connectToMySQL('chabella').query_db(query,data)
        print(result)
        return cls(result[0])

    @staticmethod
    def validate_register(user):
        is_valid=True
        query="select * from user where email=%(email)s"
        result=connectToMySQL('chabella').query_db(query,user)
        if  len(result)>=1:
            flash('Email already taken','register')
            is_valid=False
        if len(user['first_name'])<3:
            flash('First name  must be at  least 3 characters','register')
            is_valid=False
        if len(user['last_name'])<3:
            flash('Last name  must be at  least 3 characters','register')
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid Email!','register')
            is_valid=False
        if len(user['password'])<4:
            flash('Password  must be at  least 4 characters','register')
            is_valid=False
        if user['password'] != user['confirm']:
            flash("Passwords don't match",'register')
        return is_valid
    
