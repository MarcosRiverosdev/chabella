from chabella import app
from flask import render_template,redirect,request,session,flash
from chabella.models.category import Category
from flask_bcrypt import Bcrypt
bcrypt=Bcrypt(app)


@app.route('/categories')
def categories():
    return render_template('admin_new_category.html',categories=Category.get_all_categories())

@app.route('/category/add', methods=['POST'])
def newcategories():
    if not Category.validate_register(request.form):
        return redirect('/categories')
    data={
        "category" : request.form['category'],
    }
    Category.save_category(data)
    return redirect('/new/product')


