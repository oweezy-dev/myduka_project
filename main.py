from flask import Flask,render_template,request,redirect,url_for#plan
from database import fetch_data,insert_products,insert_sales,insert_stock,calculate_profit,calculate_sales
#instance of the flask class
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

#route for dashboard
@app.route('/dashboard')
def dashboard():
    profits=calculate_profit()
    sales=calculate_sales()
    #print(sales)
    #print(profit)
    product_names=[]
    product_profits=[]
    for profit in profits:
        product_names.append(profit[0])
        product_profits.append(float(profit[2]))

    product_sales=[]    
    products_names=[]    
    for sale in sales:
        products_names.append(sale[0])
        product_sales.append(float(sale[2]))


        
       
    return render_template('dashboard.html',product_names=product_names,product_profits=product_profits,product_sales=product_sales,products_names=products_names)


@app.route('/products')
def prods():
    prods=fetch_data('products')
   
    return render_template('products.html',products=prods)

#create a python function that receives data from the ui to the serverside
@app.route('/add_products',methods=['GET','POST'])
def add_products():
    #checking method
    if request.method=='POST':
        #get form data/input
        pname=request.form['product name']
        bprice=request.form['buying price']
        sprice=request.form['selling price']
        new_product=(pname,bprice,sprice)
        #insert to the database by calling the function
        insert_products(new_product)
        return redirect(url_for('prods'))
        

    
#route for sales
@app.route('/sales')
def sales1():
    sales=fetch_data('sales')
    products=fetch_data('products')#table to fetch from
    
    return render_template('sales.html',sls=sales,products=products)
#create a python function that receives data from the ui to the serverside
@app.route('/add_sales',methods=['GET','POST'])
def add_sales():
     #checking method
    if request.method=='POST':
        #get form data/input
        pid=request.form['product_id']
        quantity=request.form['Quantity']
        new_sale=(pid,quantity)
        #insert to the database by calling the function
        insert_sales(new_sale)
        return redirect(url_for('sales1'))#url for takes the function name

#route for stock
@app.route('/stocks')
def stock1():
    stocks=fetch_data('stock')
    products=fetch_data('products')#table to fetch from
   
    return render_template('stocks.html',stocks=stocks,products=products)

#create a python function that receives data from the ui to the serverside
@app.route('/add_stocks',methods=['GET','POST'])
def add_stocks():
     #checking method
    if request.method=='POST':
        #get form data/input
        pid=request.form['Product_id']
        stock_qty=request.form['stock_quantity']
        new_stock=(pid,stock_qty)
        #insert to the database by calling the function
        insert_stock(new_stock)
        return redirect(url_for('stock1'))#url for takes the function name

#run the app
app.run(debug=True)