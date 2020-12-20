import os
from flask import Flask, render_template, request, url_for, flash,redirect
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


 # Routes to  "cocktails by categories"   
@app.route('/get_coctail_by_category/<category>')
def get_coctail_by_category(category):
    category_name = category
    return render_template('coctails_by_category.html',
     coctails=list(mongo.db.coctails.find({"category_name":category}).sort("coctail_name")), category_name=category_name)
       
       
# routes page to all cocktails in my DB   
@app.route('/get_coctail')
def get_coctail():
    return render_template('allcoctails.html', 
                           # sorts list to last inserted doc to help users find it easily.
                           coctails=mongo.db.coctails.find().sort("_id", -1))




# page to add a new cocktail
@app.route('/add_coctail', methods=["GET", "POST"])
def add_coctail():
 
    if request.method == "POST":
      
        coctail= {
            "category_name": request.form.get("category_name"),
            "image_link": request.form.get("image_link"),
            "coctail_name": request.form.get("coctail_name"),
            "type": request.form.get("type"),
            "primary_alcohol": request.form.get("primary_alcohol"),
            "served": request.form.get("served"),
            "drinkware": request.form.get("drinkware"),
            "ingredients": request.form.get("ingredients"),
            "preparation": request.form.get("preparation"),
            "notes": request.form.get("notes"),
            
        }

        

        mongo.db.coctails.insert_one(coctail)
        flash("Task Successfully Added")
        return redirect(url_for("get_coctail"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("addcoctail.html",  categories=categories)


# inserts new cocktail
@app.route('/insert_coctail', methods=['GET', 'POST'])
def insert_coctail():
    coctails =  mongo.db.coctails
    coctails.insert_one(request.form.to_dict())
    return redirect(url_for('get_coctails'))    


 # Edit/update new cocktail
    
@app.route("/edit_coctail/<coctail_id>", methods=["GET", "POST"])
def edit_coctail(coctail_id):
    if request.method == "POST":
        
        submit = {
            
            "category_name": request.form.get("category_name"),
            "image_link": request.form.get("image_link"),
            "coctail_name": request.form.get("coctail_name"),
            "type": request.form.get("type"),
            "primary_alcohol": request.form.get("primary_alcohol"),
            "served": request.form.get("served"),
            "drinkware": request.form.get("drinkware"),
            "ingredients": request.form.get("ingredients"),
            "preparation": request.form.get("preparation"),
            "notes": request.form.get("notes"),
        }
        mongo.db.coctails.update_one({"_id": ObjectId(coctail_id)}, {"$set": submit})
        flash("Task Successfully Updated")
        return redirect(url_for("show_coctail", coctail_id=coctail_id))

    coctail = mongo.db.coctails.find_one({"_id": ObjectId(coctail_id)})
    print(coctail)
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_coctail.html", coctail=coctail, categories=categories)




                           
# routes to view cocktail information
@app.route("/show_coctail/<coctail_id>")
def show_coctail(coctail_id):
        the_coctail = mongo.db.coctails.find_one({"_id": ObjectId(coctail_id)})
        all_categories = mongo.db.category.find()
        return render_template('showcoctail.html', coctail=the_coctail, categories=all_categories)
    


 # Removew cocktail
@app.route("/delete_coctail/<coctail_id>", methods=["GET", "POST"])
def delete_coctail(coctail_id):
    mongo.db.coctails.remove({"_id": ObjectId(coctail_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("get_coctail"))


 # Route to page that displays top cocktail bartenders.
@app.route('/stars')
def stars():
    return render_template('stars.html')
                          



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)