#################################################
# Load Dependencies
#################################################

# Import SQL Alchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import Column, Integer,Float, String,  create_engine
from sqlalchemy.orm import Session

Base = declarative_base()
engine = None

# Import flask
from flask import Flask, request, jsonify, render_template, after_this_request

#################################################
# Database Setup
#################################################

# Set database path and engine
dbPath = 'sqlite:///project_2.sqlite'
engine = create_engine(dbPath, connect_args={'check_same_thread': False})

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# # Save reference to the table
# Earthquake = Base.classes.seismic_data
# Relief = Base.classes.relief_expenses
# Quaker = Base.classes.quakers2shakers

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def open():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("vizDashboard.html")

@app.route("/playground")
def playground():
    return render_template("earthquakePlayground.html")

@app.route("/machinelearning")
def machinelearning():
    return render_template("machineLearning.html")

# @app.route("/routes")
# def routes(): 
#     print("Server access home")
#     return(
#         f"project 2: earthquake data API<br>"
#         f"Available routes:<br>"
#         f"/api/v1.0/earthquake_data<br>"
#         f"/api/v1.0/relief_data"
#     )

# @app.route("/api/v1.0/earthquake_data")
# def earthquakes():
#     print("Server access earthquake data")
#     s = Session(bind=engine)

#     results = s.query(Earthquake.id, Earthquake.Latitude, Earthquake.Longitude, Earthquake.Depth,
#     Earthquake.Magnitude, Earthquake.Waveform, Earthquake.Place, Earthquake.Time, Earthquake.Type
#     ).all()

#     s.close()

#     earthquake_data = []
#     for id, Latitude, Longitude, Depth, Magnitude, Waveform, Place, Time, Type in results:
#         earthquake_dict = {}
#         earthquake_dict["id"] = id
#         earthquake_dict["Latitude"] = Latitude
#         earthquake_dict["Longitude"] = Longitude
#         earthquake_dict["Depth"] = Depth
#         earthquake_dict["Magnitude"] = Magnitude
#         earthquake_dict["Waveform"] = Waveform
#         earthquake_dict["Place"] = Place
#         earthquake_dict["Time"] = Time
#         earthquake_dict["Type"] = Type
#         earthquake_data.append(earthquake_dict)

#     return jsonify(earthquake_data)

# @app.route("/api/v1.0/relief_data")
# def earthquake_relief():
#     print("Server access relief data")
#     s = Session(bind=engine)

#     results = s.query(Relief.id, Relief.Country, Relief.Total_relief
#     ).all()

#     s.close()

#     relief_data = []
#     for id, Country, Total_relief in results:
#         relief_dict = {}
#         relief_dict["id"] = id
#         relief_dict["Country"] = Country
#         relief_dict["Total_relief"] = Total_relief
#         relief_data.append(relief_dict)

#     return jsonify(relief_data)

# @app.route("/api/v1.0/quaker_data")
# def quakers():
#     print("Server access quaker2shaker data")
#     s = Session(bind=engine)

#     results = s.query(Quaker.id, Quaker.country, Quaker.magnitude, Quaker.pop_mil, Quaker.aid_usd_mil,
#     Quaker.earthqks_year_prev)

#     s.close()

#     quaker_data = []
#     for id, country, magnitude, pop_mil, aid_us_mil, earthqks_year_prev in results:
#         quaker_dict = {}
#         quaker_dict["id"] = id
#         quaker_dict["country"] = country
#         quaker_dict["magnitude"] = magnitude
#         quaker_dict["pop_mil"] = pop_mil
#         quaker_dict["aid_us_mil"] = aid_us_mil
#         quaker_dict["earthqks_year_prev"] = earthqks_year_prev
#         quaker_data.append(quaker_dict)

#     return jsonify(quaker_data)

if __name__=="__main__":
    app.run(debug = True)