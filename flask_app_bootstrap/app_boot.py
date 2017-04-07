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
import psycopg2

from flask import Flask, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

################################################################
#Conenction to SQL
#host: appdev.cuq8d0oymhgs.us-west-2.rds.amazonaws.com
#port: 5432
#dbname: numinous
#username: stanley
#password: Msan4ever!
#conn = psycopg2.connect("port=5432 dbname='numinous' user='stanley' host='appdev.cuq8d0oymhgs.us-west-2.rds.amazonaws.com' password='Msan4ever!'")
#cur = conn.cursor()
#cur.execute("""SELECT datname from pg_database""")
#rows = cur.fetchall()
#print "\nShow me the databases:\n"
#for row in rows:
#    print "   ", row[0]

#conn.close()
################################################################

app = flask.Flask(__name__)

@app.route("/")
def home_page():
    """
    When you request the root path, flask will return the landing page  html.
    """
    return flask.render_template("index.html")


@app.route("/tables")
def tables():
    """
    When you request the root path, you'll get the index.html template.
    """
    return flask.render_template("tables.html")

@app.route("/input_info")
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
