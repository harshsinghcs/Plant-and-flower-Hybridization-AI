from flask import Flask, render_template, request
import random

app = Flask(__name__)

class Plant:
    def __init__(self, traits):
        self.traits = traits

def hybridize(parent1, parent2):
    if len(parent1.traits) != len(parent2.traits):
        raise ValueError("Parents must have the same number of traits")
    
    child_traits = []
    for trait1, trait2 in zip(parent1.traits, parent2.traits):
        child_trait = random.choice([trait1, trait2])
        child_traits.append(child_trait)
    
    return Plant(child_traits)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        parent1_traits = [request.form[f"parent1_{trait}"] for trait in trait_names]
        parent2_traits = [request.form[f"parent2_{trait}"] for trait in trait_names]
        
        parent1 = Plant(parent1_traits)
        parent2 = Plant(parent2_traits)
        
        child = hybridize(parent1, parent2)
        
        return render_template("index.html", parent1=parent1, parent2=parent2, child=child)
    
    return render_template("index.html")

if __name__ == "__main__":
    trait_names = ["Height", "Color", "Bloom Time"]
    app.run(debug=True)
