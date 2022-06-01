# first ctrl+shift+p
# type: python: select interpreter
# choose "pythonData" environment that we have created before
# then run the code below
from flask import Flask

#Create a New Flask App Instance
#Variables with underscores before and after them are called magic methods in Python
app = Flask(__name__)

#Create Flask Routes 
#define the starting point, also known as the root
@app.route('/')
def hello_world():
    return 'Hello world'

#Run a Flask App
#need to run this from command line (navigate to to weher this code is saved from Anaconada command line)
# run 
#   1: set FLASK_APP=app.py 
#   2: flask run

# When you run this command, you'll notice a line that says "Running on" followed by an address. 
# This should be your localhost address and a port number.
# Copy and paste your localhost address into your web browser. 
# http://127.0.0.1:5000/
