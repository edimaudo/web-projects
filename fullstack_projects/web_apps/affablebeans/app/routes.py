from flask import Flask, render_template
from app import app

@app.route('/')
@app.route('/index')
@app.route('/affablebeans')
def index():
    return render_template("index.html")

@app.route('/cart')
def cart():
    return render_template("cart.html")

@app.route('/category')
def category():
    return render_template("category.html")

@app.route('/confirmation')
def confirmation():
    return render_template("confirmation.html")

@app.route('/checkout')
def checkout():
    return render_template("checkout.html")

#Make updates to all options below
@app.route('/addtocart')
def addtocart():
    return render_template("cart.html")


@app.route('/viewcart')
def viewcart():
    return render_template("cart.html")

@app.route('/updatecart')
def updatecart():
    return render_template("cart.html")

@app.route('/purchase')
def purchase():
    return render_template("cart.html")

@app.route('/chooselanguage')
def chooselanguage():
    return render_template("cart.html")