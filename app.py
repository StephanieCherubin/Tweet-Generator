from flask import Flask
from dictionary_words import dictionary_words

app = Flask(__name__)

@app.route('/')
def hello_world():
    variable = dictionary_words(50)
    return variable

    

if __name__ == '__main__':
    hello_world()
    