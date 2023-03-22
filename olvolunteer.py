from flask import Flask
import random
import pyjokes


# file = open("class.txt", "r")

# file_lines = file.read()
# list_of_lines = file_lines.split("\n")
# My_joke = pyjokes.get_joke(language="en", category="neutral")

# print("I nominate  " + random.choice(list_of_lines))

# print("The Joke of the day is:  " + My_joke)

app=Flask(__name__)
  
  
@app.route("/")
def home():
    #background-image: url({{ url_for('static', filename='img/laugh.jpg') }})
    joke=pyjokes.get_joke(language="en", category="neutral")  #It only returns one joke. We get random joke each time. 
    return f'<h2>{joke}</h2>'
  
@app.route("/volunteer")
def jokes():
    file = open("class.txt", "r")

    file_lines = file.read()
    list_of_lines = file_lines.split("\n")
    nominee=random.choice(list_of_lines)  #Here, we get a list of jokes.  
    return f'<h2>{nominee}</h2>'
  
if __name__ == "__main__":
    app.run(debug=True)