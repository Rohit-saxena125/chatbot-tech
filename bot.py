import numpy as np
import pandas as pd
import aiml
import json
import roadmap
import flask
import os

app = flask.Flask(__name__)

# Initialize the AIML kernel and load the AIML files
kernel = aiml.Kernel()
kernel.learn("startup.xml")
kernel.respond("load aiml b")

# Define the route for the home page
@app.route('/')
def home():
    return flask.render_template('index.html')

# Define the route for handling user input and returning the bot's response
@app.route('/get_response', methods=['POST'])
def get_bot_response():
    user_input = flask.request.form['user_input']
    if 'roadmap' in user_input:
        response = roadmap.get_roadmap(user_input.split(' ')[0])
    else:
        response = get_response(user_input)
    return response

# Define a function to search the JSON file for the user's input
def get_response(input_text):
    response = search_json_file(input_text)
    return response

# Define a function to search the JSON file
def search_json_file(key):
    try:
        if len(key.split(' ')) > 1:
            key = key.split(' ')
            with open('sample.json') as f:
                data = json.load(f)
                return data['techname'][key[0]][key[1]]
        else:
            with open('sample.json') as f:
                data = json.load(f)
                if key in data['techname'].keys():
                    return f"{data['techname'][key]['techdesc']} \n  {data['techname'][key]['techlink']} \n"
                return {data['techname'][key].values()}
    except:
        return "Sorry, I don't know that one yet. I am still learning."

if __name__ == '__main__':
    app.run(debug=True)
