import os
from flask import Flask, render_template, request, url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.objectid import ObjectId


if os.path.exists("env.py"):
    import env
    

app = Flask(__name__)

#Configuration to grab the database name
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")


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


 # Routes to  "coctails by categories"   
@app.route('/get_coctail_by_category/<category>')
def get_coctail_by_category(category):
    return render_template('coctails_by_category.html',
     coctails=mongo.db.coctails.find({"category_name":category}).sort("coctail_name"))     
       
       
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