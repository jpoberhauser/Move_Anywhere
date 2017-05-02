import psycopg2
from flask import Flask, make_response
import json
import flask
import numpy as np
import pandas as pd

app = flask.Flask(__name__)

@app.route("/")
def show_home():
    return "Home"


@app.route("/schools")
def show_sc():
    return schools.to_json(orient="records")


@app.route("/events")
def show_events():
    return events.to_json(orient="records")


@app.route("/jobs")
def show_jobs():
    return jobs.to_json(orient="records")


if __name__ == "__main__":
    import os
    port = 8000
    conn = psycopg2.connect("port=5432 dbname='numinous' user='stanley' host='appdev.cuq8d0oymhgs.us-west-2.rds.amazonaws.com' password='Msan4ever!'")
    cur = conn.cursor()
    #cur.execute("""SELECT datname from pg_database""")
    cur.execute("""SELECT * from jobs limit 50""")
    jobs = pd.DataFrame(cur.fetchall(), columns=['id', 'city', 'job_id',
    'title','url','company','snippet','state','date_posted'])


    cur = conn.cursor()
    #cur.execute("""SELECT datname from pg_database""")
    cur.execute("""SELECT * from events limit 50""")
    events = pd.DataFrame(cur.fetchall(), columns=['event_name', 'city', 'event_description',
    'event_date','date_added'])


    cur = conn.cursor()
    #cur.execute("""SELECT datname from pg_database""")
    cur.execute("""SELECT * from schools limit 50""")
    schools = pd.DataFrame(cur.fetchall(), columns=['id', 'city','name', 'phone',
    'reviewslink','enrollment','parentrating','lon','overviewlink','gsid','state','address',
    'lat','type','graderange','ratingslink'])


    conn.close()
    # Open a web browser pointing at the app.
    os.system("open http://localhost:{0}".format(port))
    # Set up the development server on port 8000.
    app.debug = True
    app.run(host='0.0.0.0')
    app.run(port=port)
