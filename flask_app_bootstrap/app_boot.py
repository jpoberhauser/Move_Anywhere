import json
import flask
import numpy as np
import pandas as pd
import random
import StringIO
import psycopg2

from flask import Flask, make_response

################################################################
################################################################

app = flask.Flask(__name__)

@app.route("/")
def home_page():
    """
    When you request the root path, flask will return the landing page  html.
    """
    return flask.render_template("index.html")

@app.route("/v2")
def home_page2():
    """
    When you request the root path, flask will return the landing page  html.
    """
    return flask.render_template("index2.html")

@app.route("/v3")
def home_page3():
    """
    When you request the root path, flask will return the landing page  html.
    """
    return flask.render_template("index3.html")


@app.route("/v4")
def home_page4():
    """
    When you request the root path, flask will return the landing page  html.
    """
    return flask.render_template("index4.html")
    
@app.route("/input_info")
def input_form():
    """
    When you request the root path, you'll get the index.html template.
    """
    return flask.render_template("input_form.html")

@app.route("/NYC")
def show_j_nyc():
    cur.execute("""SELECT city,title,company, snippet from jobs where city='New York' limit 2""")
    jobs = pd.DataFrame(cur.fetchall(), columns=[ 'city',
    'title','company','snippet'])


    cur.execute("""SELECT event_name, event_description, event_date, city from events where city='New+York,+NY' limit 2""")
    events = pd.DataFrame(cur.fetchall(), columns=['event_name', 'event_description',
    'event_date','city'])

    cur.execute("""SELECT name, phone, reviewslink, ratingslink from schools where city='New York' limit 2""")
    schools = pd.DataFrame(cur.fetchall(), columns=['name', 'phone',
    'reviewslink','ratingslink'])


    return flask.render_template('view.html',tables=[jobs.to_html(classes='jobs'),events.to_html(classes='events'),
    schools.to_html(classes='schools')],
    titles = ['na', 'Jobs', 'Events','Schools'])

@app.route("/Austin")
def show_j_austin():
    cur.execute("""SELECT city,title,company, snippet from jobs where city='Austin' limit 2""")
    jobs = pd.DataFrame(cur.fetchall(), columns=[ 'city',
    'title','company','snippet'])


    cur.execute("""SELECT event_name, event_description, event_date, city from events where city='Austin,+TX' limit 2""")
    events = pd.DataFrame(cur.fetchall(), columns=['event_name', 'event_description',
    'event_date','city'])

    cur.execute("""SELECT name, phone, reviewslink, ratingslink from schools where city='Austin' limit 2""")
    schools = pd.DataFrame(cur.fetchall(), columns=['name', 'phone',
    'reviewslink','ratingslink'])

    return flask.render_template('view.html',tables=[jobs.to_html(classes='jobs'),events.to_html(classes='events'),
    schools.to_html(classes='schools')], titles = ['na', 'Jobs', 'Events','Schools'])

@app.route("/SF")
def show_j_san_fran():
    cur.execute("""SELECT city,title,company, snippet from jobs where city='San Francisco' limit 2""")
    jobs = pd.DataFrame(cur.fetchall(), columns=[ 'city',
    'title','company','snippet'])


    cur.execute("""SELECT event_name, event_description, event_date, city from events where city='San+Francisco,+CA' limit 2""")
    events = pd.DataFrame(cur.fetchall(), columns=['event_name', 'event_description',
    'event_date','city'])

    cur.execute("""SELECT name, phone, reviewslink, ratingslink from schools where city='San Francisco' limit 2""")
    schools = pd.DataFrame(cur.fetchall(), columns=['name', 'phone',
    'reviewslink','ratingslink'])

    return flask.render_template('view.html',tables=[jobs.to_html(classes='jobs'),events.to_html(classes='events'),
    schools.to_html(classes='schools')], titles = ['na', 'Jobs', 'Events','Schools'])

@app.route("/Chicago")
def show_j_chicago():
    cur.execute("""SELECT city,title,company, snippet from jobs where city='Chicago' limit 2""")
    jobs = pd.DataFrame(cur.fetchall(), columns=[ 'city',
    'title','company','snippet'])

    cur.execute("""SELECT event_name, event_description, event_date, city from events where city='Chicago,+IL' limit 2""")
    events = pd.DataFrame(cur.fetchall(), columns=['event_name', 'event_description',
    'event_date','city'])

    cur.execute("""SELECT name, phone, reviewslink, ratingslink from schools where city='Chhicago' limit 2""")
    schools = pd.DataFrame(cur.fetchall(), columns=['name', 'phone',
    'reviewslink','ratingslink'])

    return flask.render_template('view.html',tables=[jobs.to_html(classes='jobs'),events.to_html(classes='events'),
    schools.to_html(classes='schools')], titles = ['na', 'Jobs', 'Events','Schools'])

@app.route("/Boston")
def show_j_bost():
    cur.execute("""SELECT city,title,company, snippet from jobs where city='Boston' limit 2""")
    jobs = pd.DataFrame(cur.fetchall(), columns=[ 'city',
    'title','company','snippet'])


    cur.execute("""SELECT event_name, event_description, event_date, city from events where city='Boston,+MA' limit 2""")
    events = pd.DataFrame(cur.fetchall(), columns=['event_name', 'event_description',
    'event_date','city'])

    cur.execute("""SELECT name, phone, reviewslink, ratingslink from schools where city='Boston' limit 2""")
    schools = pd.DataFrame(cur.fetchall(), columns=['name', 'phone',
    'reviewslink','ratingslink'])

    return flask.render_template('view.html',tables=[jobs.to_html(classes='jobs'),events.to_html(classes='events'),
    schools.to_html(classes='schools')], titles = ['na', 'Jobs', 'Events','Schools'])

@app.route("/Miami")
def show_j_miami():
    cur.execute("""SELECT city,title,company, snippet from jobs where city='Miami' limit 2""")
    jobs = pd.DataFrame(cur.fetchall(), columns=[ 'city',
    'title','company','snippet'])

    cur.execute("""SELECT event_name, event_description, event_date, city from events where city='Miami,+FL' limit 2""")
    events = pd.DataFrame(cur.fetchall(), columns=['event_name', 'event_description',
    'event_date','city'])

    cur.execute("""SELECT name, phone, reviewslink, ratingslink from schools where city='Miami' limit 2""")
    schools = pd.DataFrame(cur.fetchall(), columns=['name', 'phone',
    'reviewslink','ratingslink'])

    return flask.render_template('view.html',tables=[jobs.to_html(classes='jobs'),events.to_html(classes='events'),
    schools.to_html(classes='schools')], titles = ['na', 'Jobs', 'Events','Schools'])



@app.route("/tables")
def show_tables():
    return flask.render_template('view.html',tables=[jobs.to_html(classes='jobs'),events.to_html(classes='events'),
    schools.to_html(classes='schools')],
    titles = ['na', 'Jobs', 'Events','Schools'])

if __name__ == "__main__":
    import os
    port = 8000
    conn = psycopg2.connect("port=5432 dbname='numinous' user='stanley' host='appdev.cuq8d0oymhgs.us-west-2.rds.amazonaws.com' password='Msan4ever!'")
    cur = conn.cursor()
    #cur.execute("""SELECT datname from pg_database""")

    cur = conn.cursor()
    #cur.execute("""SELECT datname from pg_database""")
    cur.execute("""SELECT * from events limit 100""")
    events = pd.DataFrame(cur.fetchall(), columns=['event_name', 'city', 'event_description',
    'event_date','date_added'])


    cur = conn.cursor()
    #cur.execute("""SELECT datname from pg_database""")
    cur.execute("""SELECT * from schools limit 100""")
    schools = pd.DataFrame(cur.fetchall(), columns=['id', 'city','name', 'phone',
    'reviewslink','enrollment','parentrating','lon','overviewlink','gsid','state','address',
    'lat','type','graderange','ratingslink'])



    # Open a web browser pointing at the app.
    os.system("open http://localhost:{0}".format(port))
    # Set up the development server on port 8000.
    app.debug = True

    app.run(port=80, host='0.0.0.0')