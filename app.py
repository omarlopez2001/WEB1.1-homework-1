from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/penguins')
def penguins_page():
    """Shows my favorite animal to the user."""
    return 'Penguins are cute!'

@app.route('/lions')
def lions_page():
    """Shows my favorite animal to the user."""
    return 'Lions are the kings of the wild!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Displays a message to the user that changes based on their favorite dessert"""
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def madlib(adjective, noun):
    """Displays a funny madlib using the users' adjective and noun"""
    return f'I can\'t believe {adjective} dogs like to sniff {noun}!'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    result = int(number1) * int(number2)
    """Multiplies number1 and number2 and displays the result"""
    return f'{number1} times {number2} is {result}.'

@app.route('/reverse/<word>')
def reverse(word):
    reverse_word = word [::-1]
    """Reverses a string""" 
    return f'{reverse_word}'

if __name__ == '__main__':
    app.run(debug=True)