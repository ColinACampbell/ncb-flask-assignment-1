from flask import Flask, render_template

PRODUCTS = [ {"name":"4x4 Ballon", "image" :"balloon.jpeg", "price":12340.23},
             {"name":"2023 Car", "image" :"car.jpeg", "price":12340.23},
              {"name":"Gucci Bag", "image" :"gucci-bag.jpeg", "price":12340.23},
               {"name":"Nike Shoes", "image" :"nike-shoes.jpeg", "price":12340.23},
               {"name":"Uraniun (From Oppenheimer)", "image" :"uranium.jpeg", "price":12340.23},
               {"name":"Macbook Pro", "image" :"macbookpro.jpeg", "price":12340.23}]

app = Flask(__name__, instance_relative_config=True)

@app.route('/')
def home():
    return PRODUCTS

@app.route('/products')
def products_page():
    return render_template('products.html', products = PRODUCTS)


@app.route('/products/<product_id>')
def product_page(product_id:int):
    return render_template('products.html')

# run with this flask --app main.py --debug run