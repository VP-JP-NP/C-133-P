# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Veda Patel"
    age = "13"

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def first_flask():
    return "I am the father."

# define the route to mother webpage
@app.route("/mother")
def second_flask():
    return "I am the mother."

# define the route to friends webpage
@app.route("/friend")
def third_flask():
    return "I am the friend."

# add other routes, if you want
@app.route("/grandparents")
def fourth_flask():
    return "We are the grandparents."



# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
