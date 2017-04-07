import json
import flask
import numpy as np
import pandas as pd
import random
import StringIO
import matplotlib.pyplot as plt
import seaborn as sns
import StringIO
import base64

from flask import Flask, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


app = flask.Flask(__name__)

@app.route("/")
def home_page():
    """
    When you request the root path, you'll get the index.html template.
    """
    return flask.render_template("index.html")


@app.route("/tables")
def tables():
    """
    When you request the root path, you'll get the index.html template.
    """
    return flask.render_template("tables.html")

@app.route("/test")
def hello():
    """
    When you request the root path, you'll get the index.html template.
    """
    return flask.render_template("input_form.html")



if __name__ == "__main__":
    import os
    port = 8000
    # Open a web browser pointing at the app.
    os.system("open http://localhost:{0}".format(port))
    # Set up the development server on port 8000.
    app.debug = True
    app.run(port=port)
