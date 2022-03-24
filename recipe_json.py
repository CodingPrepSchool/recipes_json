from flask import Flask, render_template, request
import json
from form import RecipeForm


app= Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'


file_connection = open("C:/code/github/recipes_json/all_recipes.json", 'r')
recipe = json.load(file_connection)
file_connection.close()


@app.route("/")
def index():
    new_recipe = RecipeForm(csrf_enabled=False)
    return render_template("index.html",recipe = recipe, template_form = new_recipe)


file_connection = open("C:/code/github/recipes_json/all_recipes.json", 'r')
recipe = json.load(file_connection)
file_connection.close()

@app.route("/recipe/add",methods=["GET", "POST"])
def feedback():
    new_recipe = RecipeForm(csrf_enabled=False)
    if new_recipe.validate_on_submit():
        id = len(recipe) + 1
        recipe.append({
            "name": new_recipe.name.data,
            "ingredients": new_recipe.ingredients.data.split(","),
            "instructions": new_recipe.instructions.data.split(","),
            })
        file_connection = open("C:/code/github/recipes_json/all_recipes.json", 'w')
        json.dump(recipe, file_connection)
        file_connection.close()
    return render_template("index.html",template_form = new_recipe, recipe = recipe)




@app.route("/recipe/<int:id>", methods = ["GET","POST"])
def recipes_function(id):
    json_dict = recipe[id -1]
    name = json_dict["name"]
    ingredients = json_dict["ingredients"]
    instructions = json_dict["instructions"]
    return render_template("all_recipes.html", recipe=recipe, name = name,ingredients = ingredients,instructions=instructions)