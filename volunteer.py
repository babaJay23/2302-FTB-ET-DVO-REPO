from flask import Flask, render_template
import random
import pyjokes
import randfacts

app = Flask(__name__)

# @app.route("/")
# def home():
#     joke = pyjokes.get_joke(language="en", category="neutral")
#     return render_template("jokes.html", joke=joke)

@app.route("/")
def home():
    links = [
        {"url": "/jokes", "name": "Jokes"},
        {"url": "/volunteer", "name": "Volunteer"},
        {"url": "/facts", "name": "Random Facts"},
    ]
    return render_template("index.html", links=links)

@app.route("/jokes")
def jokes():
    joke = pyjokes.get_joke(language="en", category="neutral")
    return render_template("jokes.html", joke=joke)

@app.route("/volunteer")
def volunteer():
    file = open("class.txt", "r")
    file_lines = file.read()
    list_of_lines = file_lines.split("\n")
    nominee = random.choice(list_of_lines)
    return render_template("volunteer.html", nominee=nominee)
#random facts
@app.route("/facts")
def facts():
    facts = randfacts.get_fact()
    return render_template("facts.html", facts=facts)

if __name__ == "__main__":
    app.run(debug=True)