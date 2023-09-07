from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)


class Plant:
    def __init__(self, traits):
        self.traits = traits

    @staticmethod
    def hybridize(plant1, plant2):
        combined_traits = [random.choice(trait_pair) for trait_pair in
                           zip(plant1.traits, plant2.traits)]
        return Plant(combined_traits)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/hybridize", methods=["POST"])
def hybridize_plants():
    parent1_traits = [request.form["parent1_height"],
                      request.form["parent1_color"]]  # Add more traits
    parent2_traits = [request.form["parent2_height"],
                      request.form["parent2_color"]]  # Add more traits

    parent1 = Plant(parent1_traits)
    parent2 = Plant(parent2_traits)

    child = Plant.hybridize(parent1, parent2)

    response = {
        "parent1_traits": parent1.traits,
        "parent2_traits": parent2.traits,
        "child_traits": child.traits
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
