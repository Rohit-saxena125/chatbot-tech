import numpy as np
import pandas as pd
import aiml
import json
import roadmap
import flask
import os
kernel = aiml.Kernel()

kernel.learn("startup.xml")
kernel.respond("load aiml b")
def get_response(input_text):
    response = search_json_file(input_text)
    return response
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
                return {data['techname'][key]}
    except:
        return "Sorry, I don't know that one yet. I am still learning."
print("hii")
while True:
    user_input = input("You:")
    if 'roadmap' in user_input:
        print("Bot: " + roadmap.get_roadmap(user_input.split(' ')[0]))
    else:
        print("Bot: " + str(get_response(user_input)))