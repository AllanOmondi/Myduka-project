from flask import Flask,render_template,request,redirect,url_for
from database import fetch_data,insert_products,insert_sales,insert_stock,product_profit,product_sales

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

#products route
@app.route('/products')
def products():
    prods=fetch_data('products')
    # print(prods)
    return render_template ('products.html',total_products=prods)

@app.route('/add_products',methods=['POST','GET'])
def add_products():
    if request.method=='POST':
        pname = request.form['name']
        bp = request.form['buying_price']
        sp = request.form['selling_price']

        new_products=(pname,bp,sp)
        insert_products(new_products)
        return redirect(url_for('products'))
    return redirect(url_for('total_products'))



# sales route
@app.route('/sales')
def sales():
    sales=fetch_data('sales')
    prods=fetch_data('products')
    # return render_template ('sales.html',total_products=prods)
    
    # print(sales)
    return render_template ('sales.html',total_sales=sales,total_products=prods)

    
@app.route('/add_sales',methods=['POST','GET'])
def add_sales():
    if request.method=='POST':
        pid = request.form['pid']
        q = request.form['quantity']

        new_sales=(pid,q)
        insert_sales(new_sales)
        return redirect(url_for('sales'))
    return redirect(url_for('sales'))


#stock route
@app.route('/stock')
def stock():
    stock=fetch_data('stock')
    prods=fetch_data('stock')
    # print(stock)
    return render_template ('stocks.html',total_stock=stock,total_products=prods)

@app.route('/add_stock',methods=['POST','GET'])
def add_stock():
    if request.method=='POST':
        pid = request.form['pid']
        sq = request.form['stock_quantity']

        new_stock=(pid,sq)
        insert_stock(new_stock)
        return redirect(url_for('stock'))
    return redirect(url_for('stock'))


@app.route('/dashboard')
def dashboard():
    profits=product_profit()
    # print(profits)
        
    product_names=[]
    product_profits=[]
    for i in profits: 
        product_names.append(i[0])
        product_profits.append(float (i[1]))
    # print(product_names)
    # print(product_profits)   

    total_sales=product_sales()
    sale_name=[]
    sale_product=[]
    for i in total_sales:
        sale_name.append(i[0])
        sale_product.append(float(i[2])) 
        print(sale_name)
        print(sale_product)


    return render_template('dashboard.html', product_names=product_names, product_profits=product_profits, s_name=sale_name,
    s_product=sale_product)


    
    

    










app.run(debug=True)