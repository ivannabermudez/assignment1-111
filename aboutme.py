@app.get("/")                          # we can now use our onjects method "get" as a decorator 
def index():                           # a decorator wraps a function 
    me = {                               # we create a new dictionary with key/value pairs.
        "first_name": "Ivanna",
        "last_name": "Bermudez",
        "hobbies": "Linguistics",
    
    }
    return me 
