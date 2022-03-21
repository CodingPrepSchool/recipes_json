from flask import Flask, render_template, request
import json


app= Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'


file_connection = open("C:/code/github/recipes_json/all_recipes.json", 'r')
recipe = json.load(file_connection)
file_connection.close()


@app.route("/")
def index():
    return render_template("index.html",recipe = recipe)