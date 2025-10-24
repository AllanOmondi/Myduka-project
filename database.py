import psycopg2
# connect to the postgress database

connect=psycopg2.connect(
    host='localhost',
    user='postgres',
    port=5432,
    dbname='myduka_db',
    password='08Nanyuki@27'
)
# declare cursor to perform datbase operations
curr=connect.cursor()


# fetch products
def fetch_products():
    curr.execute('select * from products;')
    prods=curr.fetchall()
    return prods

# products=fetch_products()
# print('my products')
# print(products)


#fetch sales
def fetch_sales():
    curr.execute('select * from sales;')
    sales=curr.fetchall()
    return sales
# sales=fetch_sales()
# print('my sales')
# print(sales)


#fetch stock
def fetch_stock():
    curr.execute('select * from stock;')
    stock=curr.fetchall()
    return stock
# stock=fetch_stock()
# print('my stock')
# print(stock)

# # fetch data
def fetch_data(table_name):
    curr.execute(f'select * from {table_name}')
    data=curr.fetchall()
    return data
# products=fetch_data('products')
# print(products)
# sales=fetch_data('sales')
# print(sales)
# stock=fetch_data('stock')
# print(stock)

#  # insert
# curr.execute("insert into products(name,buying_price,selling_price)values('mango',100,120);")
# connect.commit()

# curr.execute("insert into stock(pid,stock_quantity)values(5,10);")
# connect.commit()

# curr.execute("insert into sales(pid,quantity)values(5,20);")
# connect.commit()

def insert_products(values):
    query="insert into products(name, buying_price,selling_price)values(%s,%s,%s);"
    curr.execute(query,values)
    connect.commit()
# new_product=('garlic',150,170) 
# # insert_products(new_product)
# # products = fetch_data('products')
# # print(products) 

#insert sales

def insert_sales(values):
    query='insert into sales(pid,quantity,created_at)values(%s,%s,now());'
    curr.execute(query,values)
    connect.commit()

# new_sales=(5,10)
# # insert_sales(new_sales)
# sales=fetch_data('sales')
# print(sales)

#insert stock
def insert_stock(values):
    query='insert into stock(pid,stock_quantity)values(%s,%s);'
    curr.execute(query,values)
    connect.commit()

# new_stock=(5,10)
# # insert_stock(new_stock)
# stock=fetch_data('stock')
# print(stock)

# fuctions that get profit per product
def product_profit():
    query='select p.name,p.id,sum((p.selling_price-p.buying_price)*s.quantity) as total_profit from products as p join sales s on p.id=s.pid group by p.name,p.id;'
    curr.execute(query)
    profit=curr.fetchall()
    return profit

# my_profit=product_profit()
# print('total profit')
# print(my_profit)

#write a fuction that gets sales per product
def product_sales():
    query='select p.name,p.id,sum(p.selling_price*s.quantity)as total_sales from products as p join sales as s on p.id=s.pid group by p.name,p.id;'
    curr.execute(query)
    sales=curr.fetchall()
    return sales

# my_sales=product_sales()
# print('total sales')
# print(my_sales)





