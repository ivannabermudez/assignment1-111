"""sample hello world flask app"""

from flask import Flask 

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello, world!</h1>"

@app.route("/products")
def products():
    product_list = ["Apples", "Oranges", "Bananas"]
    bullet_list = "".join(
        "<li>%s</li>" % product for product in product_list
    )
    return "<ul>%s</ul>" % bullet_list

@app.get("/")                          # we can now use our onjects method "get" as a decorator 
def index():                           # a decorator wraps a function 
    me = {                               # we create a new dictionary with key/value pairs.
        "first_name": "Ivanna",
        "last_name": "Bermudez",
        "hobbies": "Linguistics",
    
    }
    return me 