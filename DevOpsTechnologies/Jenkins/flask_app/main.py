from flask import Flask
from flask import request


app = Flask("ariel's app")

foods = [{"id":1, "name":"steak", "score":99},
         {"id":2, "name":"degas parmiggiana", "score":100},
         {"id":3, "name":"carbonara", "score": 98}]


@app.route("/foods", methods=["GET", "DELETE"])
def clear_foods():
    if request.method == "DELETE":
        foods.clear()
    
    return foods


@app.route("/foods/<int:id>", methods=["GET", "POST"])
def get_id(id):
    if request.method == "GET":
        for food in foods:
            if food.get('id') == id:

                return food
            
    if request.method == "POST":
        foods.append(request.get_json())

        return {"Status":"Success"}
    
    return {}


app.run(host="0.0.0.0", port="5000")
