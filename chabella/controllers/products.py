from chabella import app
from flask import render_template,redirect,request,session,flash
from chabella.models.category import Category
from chabella.models.product import Product,Most_Sold
from chabella.models.category import Category
from flask_bcrypt import Bcrypt
bcrypt=Bcrypt(app)


@app.route('/')
def users():
    return render_template('index.html',solds=Most_Sold.get_most_vent(),products=Product.get_all_products(),categories=Category.get_all_categories())

@app.route('/new/product')
def newproduct():
    return render_template('admin_new_product.html',categories=Category.get_all_categories())

@app.route('/add/product', methods=['POST'])
def addproduct():
    if not Product.validate_register(request.form):
        return redirect('/new/product')
    data={
        "name" : request.form['name'],
        "description" : request.form['description'],
        "id_category" : request.form['id_category'],
        "image" : request.form['image'],
        "price" : request.form['price']
    }
    Product.save_product(data)
    return redirect('/new/product')

@app.route('/list/products')
def listarproductos():
    return render_template('admin_list_products.html',products=Product.get_all_products())

@app.route('/edit/product/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("admin_edit_product.html",product=Product.get_one_product(data),categories=Category.get_all_categories())

@app.route('/update/product', methods=['POST'])
def updateproduct():
    Product.update_product(request.form)
    return redirect('/list/products')

@app.route('/product/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    Product.destroy(data)
    return redirect('/list/products')

@app.route('/show/product/<int:id>')
def show_prod(id):
    data={
        'id':id
    }
    return render_template('show.html',product=Product.get_one_product(data),categories=Category.get_all_categories())

@app.route('/admin/show/<int:id>')
def admin_show_prod(id):
    data={
        'id':id
    }
    return render_template('admin_show_product.html',product=Product.get_one_product(data),categories=Category.get_all_categories())


@app.route('/category/<string:category>')
def show_category(category):
    data={
        'category':category
    }
    return render_template('show_category.html',category=Product.get_one_category(data),categories=Category.get_all_categories())
