from flask import Flask, redirect, render_template, request
import json

app=Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

file_connection = open("C:/code/github/recipes_json/all_recipies.json", 'r')
allrecipies = json.load(file_connection)
file_connection.close()
@app.route("/", methods = ["GET", "POST"])
def homepage():
    return render_template("recipie_index.html", allrecipies=allrecipies)