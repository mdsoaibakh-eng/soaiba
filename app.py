from flask import Flask, request, jsonify, render_template, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://mdsoaibakh:<db_Soaib8252>@cluster0.8fohoqg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["mydatabase"]
collection = db["mycollection"]

@app.route("/")
def index(): 
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    try:
        name = request.form.get("name")
        email = request.form.get("email")

        if not name or not email:
            return render_template("form.html", error="All fields are required.")

        # Insert into MongoDB
        collection.insert_one({"name": name, "email": email})

        return redirect(url_for("success"))

    except Exception as e:
        return render_template("form.html", error=str(e))

@app.route("/success")
def success():
    return "<h2>Data submitted successfully</h2>"

if __name__ == "__main__":
    app.run(debug=True)


       