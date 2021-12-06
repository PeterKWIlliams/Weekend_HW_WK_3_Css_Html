from flask import render_template,request,redirect
from app import app 
from models.shopping_list import *
from models.Items import *



@app.route('/items')
def index():
    return render_template('index.html',title ='Home', items = items)

@app.route('/items', methods=['POST'])
def add_item():
  name  = request.form['name']
  price = request.form['price']
  quantity = request.form['quantity']
  purchased = True if 'purchase_status' in request.form else False
  new_item = Items(name = name, price = price,quantity=quantity,purchased_status= purchased)
  add_new_item(new_item)
  return redirect('/items')
 
