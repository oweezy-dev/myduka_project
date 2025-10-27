from flask import Flask,render_template#plan
from database import fetch_data
#instance of the flask class
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def prods():
    prods=fetch_data('products')
   
    return render_template('products.html',products=prods)
#route for sales
@app.route('/sales')
def sales1():
    sales=fetch_data('sales')
    
    return render_template('sales.html',sls=sales)

#route for stock
@app.route('/stocks')
def stock1():
    stocks=fetch_data('stock')
   
    return render_template('stocks.html',stocks=stocks)

#run the app
app.run()