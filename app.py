
from flask import Flask, render_template
from flask_login import login_user
from flask import render_template, redirect
from os import path


from forms import AddProductForm, RegisterForm, LoginForm
from models import Product,  User
from extensions import app, db



if __name__ == "__main__":
    print(__name__)



@app.route("/")
def home():
   product = Product.query.all()
   return  render_template("index.html", product=product )



@app.route("/add_product", methods=["POST", "GET"] )
def add_product():
    form = AddProductForm()
    if form.validate_on_submit():
        new_product = Product(name=form.name.data, price=form.price.data, img=form.img.data.filename)
        db.session.add(new_product)
        db.session.commit()

        
        file_dir = path.join(app.root_path, "static", form.img.data.filename)
        form.img.data.save(file_dir)
        return redirect  ("/")
    return render_template("add_product.html", form=form)







@app.route("/edit_product/<int:index>", methods=["GET", "POST"] )
def edit_product(index):
    product = Product.query.get(index)
    form = AddProductForm(price=product.price, name=product.name, img=product.img)
    if form.validate_on_submit():
        product.name = form.name.data
        product.price = form.price.data
        product.img = form.img.data.filename

        file_dir = path.join(app.root_path, "static", form.img.data.filename)
        form.img.data.save(file_dir)

        db.session.commit()
        return redirect("/")
    
    return render_template("add_product.html", form=form )

@app.route("/delete_product/<int:index>")
def delete_product(index):
    product = Product.query.get(index)
    db.session.delete(product)
    db.session.commit()
    return redirect("/")



@app.route("/view_product/<int:index>")
def view_product(index):
    product = Product.query.get(index)
    return render_template("product.html", product=product[index])








@app.route("/register", methods=["GET", "POST"] )
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.usernmae.data, password=form.password.data)
        user.create()

    return render_template("registr.html", form=form)
    
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(user.username == form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
    return render_template("login.html", form=form)



@app.route("/test")
def test():
    name = "TBC Group3"
    return render_template("test.html", group_name=name)




app.run(debug=True)


