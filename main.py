from flask import Flask,render_template
from database import fetch_data

app=Flask(__name__)

@app.route('/')
def home():
    return 'hello world'

#products route
@app.route('/products')
def products():
    prods=fetch_data('products')
    # print(prods)
    return render_template ('products.html',total_products=prods)

# sales route
@app.route('/sales')
def sales():
    sales=fetch_data('sales')
    # print(sales)
    return render_template ('sales.html',total_sales=sales)

#stock route
@app.route('/stock')
def stock():
    stock=fetch_data('stock')
    # print(stock)
    return render_template ('stocks.html',total_stock=stock)











app.run()