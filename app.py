import Score

"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
import time
from flask import Flask 
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app



@app.route('/')
def hello():
    """Renders a sample page."""
    return "Hello World!"

@app.route('/score')
def score_server():
    return 
    """
    <html>
    <head>
    <title>Scores Game</title>
    </head>
    <body>
    <h1>The score is <div id="Score">{SCORE}</div></h1>
    </body>
    </html>
    """


@app.errorhandler(Exception)
def server_error(err):
    
    return 
    """
    <html>
    <head>
    <title>Scores Game</title>
    </head>
    <body>
    <body>
    <h1><div id="Score" style="color:red">{ERROR}</div></h1>
    </body>
    </html>
    """  

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
