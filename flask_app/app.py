"""
This file is part of the flask+d3 Hello World project.
"""
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
    return flask.render_template("landing.html")


@app.route("/home")
def index():
    """
    When you request the root path, you'll get the index.html template.

    """
    return flask.render_template("index.html")


@app.route("/tables")
def show_tables():
    return flask.render_template("tables.html")


@app.route('/plots')
def test():
    img = StringIO.StringIO()
    sns.set_style("dark") #E.G.
    df = pd.read_csv("../prueba.csv")
    zero_df = df.loc[df['zzz_response'] == 0]
    one_df = df.loc[df['zzz_response'] == 1]
    sns.set_style("whitegrid")
    col_name = 'NM_000018'
    ax = sns.distplot(one_df[col_name], color = "red")
    ax = sns.distplot(zero_df[col_name], color = "green")
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue())
    return flask.render_template('density.html', plot_url=plot_url)

@app.route('/correlations')
def corrs_func():
    df = pd.read_csv("/Users/jpoberhauser/Desktop/simpatica/backup_csvs/febrile_max_greater_zero.csv")
    df.drop(df.columns[0],axis=1,inplace=True)
    df = df[['zzz_response', 'NR_145479','NR_145491']]
    zero_df = df.loc[df['zzz_response'] == 0]
    zero_df = zero_df.corr()
    one_df = df.loc[df['zzz_response'] == 1]
    one_df = one_df.corr()
    one_df = one_df[:10]
    return flask.render_template('tables.html',tables=[one_df.to_html(classes='ones'), zero_df.to_html(classes='zeros')],
     titles = ['na', 'Gene Expressions: Ones', 'Gene Expressions: Zeros'])





if __name__ == "__main__":
    import os
    port = 8000
    # Open a web browser pointing at the app.
    os.system("open http://localhost:{0}".format(port))
    # Set up the development server on port 8000.
    app.debug = True
    app.run(port=port)
