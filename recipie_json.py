from flask import Flask, redirect, render_template, request
from recipie_forms import RecipieAdd
import json


app=Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

file_connection = open("C:/code/github/recipes_json/all_recipies.json", 'r')
all_recipies = json.load(file_connection)
file_connection.close()
@app.route("/", methods = ["GET", "POST"])
def homepage():
    add_recipie = RecipieAdd(csrf_enabled=False)
    return render_template("recipie_index.html", all_recipies=all_recipies, template_form = add_recipie)

@app.route("/recipe/<int:id>", methods=["GET", "POST"])
def recipe(id):
    add_recipie = RecipieAdd(csrf_enabled = False)
    json_dict = all_recipies[id-1]     
    name = json_dict["name"]
    ingredients = json_dict["ingredients"]
    instructions = json_dict["instructions"]
    return render_template("recipies_temp.html", json_dict = json_dict, name = name, ingredients = ingredients, instructions=instructions, add_recipie = add_recipie)


@app.route("/add_recipie", methods=["GET", "POST"])
def add_info():
    add_recipie = RecipieAdd(csrf_enabled = False)
    if add_recipie.validate_on_submit():
        id = len(all_recipies) + 1
        all_recipies.append({
            "id": id,
            "name": add_recipie.name.data,
            "ingredients": add_recipie.ingrediants.data.split(","),
            "instructions": add_recipie.instructions.data.split(",")})
    return redirect('/')