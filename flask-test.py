'''
Created on 

Course work: 

@author: Harshitha

Source:
    
'''
# Import necessary modules

from flask import Flask


app = Flask(__name__)

@app.route('/')
def start():

    return 'Hello world'


if __name__== "__main__":
    app.run(host="0.0.0.0", debug = True, port = 5003)