from flask import Flask 

app=Flask(__name__)

@app.route('/')
def home():
    return 'hello world'

#products route
@app.route('/products')
def products():
    return 'My products'

# sales route
@app.route('/sales')
def sales():
    return 'total sales'

#stock route
@app.route('/stock')
def stock():
    return 'total stock'











app.run()