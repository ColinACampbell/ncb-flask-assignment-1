from flask import Flask, render_template

PRODUCTS = [ {"id":1, "name":"4x4 Ballon", "image" :"balloon.jpeg", "price":12340.23, "description":""},
             {"id":2, "name":"2023 Car", "image" :"car.jpeg", "price":12340.23, "description":""},
              {"id":3, "name":"Gucci Bag", "image" :"gucci-bag.jpeg", "price":12340.23, "description":""},
               {"id":4, "name":"Nike Shoes", "image" :"nike-shoes.jpeg", "price":12340.23, "description":""},
               {"id":5, "name":"Uraniun (From Oppenheimer)", "image" :"uranium.jpeg", "price":12340.23, "description":""},
               {"id":6, "name":"Macbook Pro", "image" :"macbookpro.jpeg", "price":12340.23, "description":""}]

app = Flask(__name__, instance_relative_config=True)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products_page():
    return render_template('products.html', products = PRODUCTS)


@app.route('/products/<product_id>')
def product_page(product_id:str):




    product_id = int(product_id)
    # find the product
    page_product = None
    for product in PRODUCTS :
        # I did this because I don't want to copy and paste it x amount of times by hard coding
        product['description'] = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        if product['id'] == product_id :
            page_product = product
    
    print(page_product)

    if not (page_product  == None) :
        return render_template('product.html', product = page_product)
    else :
        return render_template('product.html', product = page_product) # TODO: Remove

# run with this flask --app main.py --debug run