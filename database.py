import psycopg2
#connect to psycopg2 database
connect=psycopg2.connect(
    host='localhost',
    user='postgres',
    port=5432,
    database='myduka_db',#dbname/database
    password='thiaree96'
)

#declare cursor to perform database operations
curr=connect.cursor()

# #fetch products
# curr.execute('select * from products;')
# prods=curr.fetchall()
# print(prods)

# #fetch sales
# curr.execute('select * from sales;')
# sale=curr.fetchall()
# print(sale)

# #fetch stock
# curr.execute('select * from stock;')
# stoc=curr.fetchall()
# print(stoc)

# #functions
# def fetch_products():
#     curr.execute('select * from products;')
#     products=curr.fetchall()
#     return products
# products=fetch_products()
# print(products)
# #fetch sales
# def fetch_sales():
#     curr.execute('select * from sales;')
#     sales=curr.fetchall()
#     return sales    
# sales=fetch_sales()
# print(sales)
# #fetch stock
# def fetch_stock():
#     curr.execute('select * from stock;')
#     stock=curr.fetchall()
#     return stock      
# stock=fetch_stock()
# print(stock)
def fetch_data(table_name):
    curr.execute(f'select * from {table_name};')
    data=curr.fetchall()
    return data
# products=fetch_data('products')
# sales=fetch_data('sales')
# stock=fetch_data('stock')
# print(products)
# print(sales)
# print(stock)

#insert stock
def insert_stock(values):
    query='insert into stock(pid,stock_quantity)values(%s,%s);'
    curr.execute(query,values)
    connect.commit()

# new_stock=(4,50)
# insert_stock(new_stock)
# stock=fetch_data('stock')
# print(stock)

# #insert products
def insert_products(values):
    query='insert into products(name,buying_price,selling_price)values(%s,%s,%s);'
    curr.execute(query,values)
    connect.commit()

# new_product=('Soap',20,25)
# insert_products(new_product)
# products=fetch_data('products')
# print(products)

# #insert sales
def insert_sales(values):
    query='insert into sales(pid,quantity,created_at)values(%s,%s,now());'
    curr.execute(query,values)
    connect.commit()

# new_sale=(2,10)
# insert_sales(new_sale)
# sales=fetch_data('sales')
# print(sales)

#profit per product
def calculate_profit():
    query='select p.name,p.id,sum((p.selling_price - p.buying_price)* s.quantity) as profit '
    'from sales as s join products as p on s.pid = p.id group by p.name, p.id;'
    curr.execute(query)
    profits=curr.fetchall()
    return profits
# myprofits=calculate_profit()
# print(f'my products total{myprofits}')

#sales per product
def calculate_sales():
    query='select p.name,p.id,sum(p.selling_price * s.quantity) as total_sales from sales' 
    ' as s join products as p on s.pid = p.id group by p.name, p.id;'
    curr.execute(query)
    sales=curr.fetchall()
    return sales
# mysales=calculate_sales() 
# print(f'my total_sales are:{mysales}')