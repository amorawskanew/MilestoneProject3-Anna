import os
from flask import Flask, render_template, request, url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.objectid import ObjectId


if os.path.exists("env.py"):
    import env
    

app = Flask(__name__)

#Configuration to grab the database name
app.config["MONGO_DBNAME"] = os.environ.get("CoctailCollections")

#Configuration for connection string
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

# To grab the secret key
app.secret_key = os.environ.get("SECRET_KEY")

#Constructer method


mongo = PyMongo(app)






# Route to home page where all the coctails are displayed
@app.route('/')
def home():
    return render_template('home.html')
    
    
# Routes to category "Classics"
@app.route('/get_classics')
def get_classics():
    return render_template('classics.html', 
                           # sort coctails in categories by coctail name
                           coctails=mongo.db.coctails.find({"category_name":"Classics"}).sort("coctail_name"))
    
    
# Routes to category "New era drinks"
@app.route('/get_new_era_drinks')
def get_new_era_drinks():
    return render_template('new_era_drinks.html', 
                           # sort coctails in categories by coctail name
                           coctails=mongo.db.coctails.find({"category_name":"New era drinks"}).sort("coctail_name"))


# Routes coctails to category "Specials"
@app.route('/get_specials')
def get_specials():
    return render_template('specials.html', 
                           # sort coctails in categories by coctail name
                           coctails=mongo.db.coctails.find({"category_name":"Specials"}).sort("coctail_name"))


# Routes coctails to category "Flaming coctails"
@app.route('/get_flaming_coctails')
def get_flaming_coctails():
    return render_template('flaming_coctails.html', 
                           # sort coctails in categories by coctail name
                           coctails=mongo.db.coctails.find({"category_name":" Flaming coctails"}).sort("coctail_name"))


# Routes coctails to category "Beer coctails"
@app.route('/get_beer_coctails')
def get_beer_coctails():
    return render_template('beer_coctails.html', 
                           # sort coctails in categories by coctail name
                           coctails=mongo.db.coctails.find({"category_name":" Beer coctails"}).sort("coctail_name"))

 
 
# Routes coctails to category "Liquor coctails"
@app.route('/get_liquor_coctails')
def get_liquor_coctails():
    return render_template('liquor_coctails.html', 
                           # sort coctails in categories by coctail name
                           coctails=mongo.db.coctails.find({"category_name":"Liquor coctails"}).sort("coctail_name")) 

# Routes coctails to category "Wine coctails"
@app.route('/get_wine_coctails')
def get_wine_coctails():
    return render_template('wine_coctails.html', 
                           # sort coctails in categories by coctail name
                           coctails=mongo.db.coctails.find({"category_name":"Wine coctails"}).sort("coctail_name")) 


# Routes coctails to category "Wine coctails"
@app.route('/get_non_alcoholic_coctails')
def get_non_alcoholic_coctails():
    return render_template('non_alcoholic_coctails.html', 
                           # sort coctails in categories by coctail name
                           coctails=mongo.db.coctails.find({"category_name":"Non-alcoholic coctails"}).sort("coctail_name")) 
           
              
# routes page to all coctails in my DB   
@app.route('/get_coctail')
def get_coctail():
    return render_template('allcoctails.html', 
                           # sorts list to last inserted doc to help users find it easily.
                           coctails=mongo.db.coctails.find().sort("_id", -1))


# page to add a new coctail
@app.route('/add_coctail')
def add_coctail():
    return render_template('addcoctail.html',
                           coctail=mongo.db.coctails.find(),
                           categories=mongo.db.category.find())   


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)