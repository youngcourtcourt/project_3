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
from flask import Flask, request, jsonify, render_template, after_this_request, current_app

#Import Pandas and JSON
import pandas as pd
import json

#Import CSV
import csv

# Import pickle
import pickle

# Import numpy
import numpy as np

#################################################
# Database Setup
#################################################

# Set database path and engine
dbPath = 'sqlite:///project_3.sqlite'
engine = create_engine(dbPath, connect_args={'check_same_thread': False})

class earthquake(Base):
    __tablename__ = 'SeismicData'
    id = Column(Integer, primary_key=True)
    Latitude = Column(String(255))
    Longitude = Column(String(255))
    Depth = Column(Float)
    Magnitude = Column(Float)
    Waveform = Column(String(255))
    Place = Column(String(255))
    Time = Column(Float)
    Type = Column(String(255))

class uncerf(Base):
    __tablename__ = 'ReliefExpenses'
    id = Column(Integer, primary_key=True)
    Country = Column(String(255))
    Total_relief = Column(Integer)

class quake(Base):
    __tablename__ = 'Quakers2Shakers'
    id = Column(Integer, primary_key=True)
    country = Column(String(255))
    magnitude = Column(Float)
    pop_mil = Column(Float)
    aid_usd_mil = Column(Float)
    earthqks_year_prev = Column(Integer)

class county_data(Base):
    __tablename__ = 'CountyData'
    id = Column(Integer, primary_key=True)
    county = Column(String(255))
    total_damaging_events = Column(Float)
    rate_of_damaging_events = Column(Float)
    frequency_of_section_1 = Column(Float)
    recurance_interval_1 = Column(Float)
    area_of_section_1 = Column(Float)
    frequency_of_section_2 = Column(Float)
    recurance_interval_2 = Column(Float)
    area_of_section_2 = Column(Float)
    probability = Column(Float)
    latitude = Column(Float)
    longitude = Column(Float)
    radius = Column(Float)

class county10_data(Base):
    __tablename__ = 'County10'
    id = Column(Integer, primary_key=True)
    county = Column(String(255))
    total_damaging_events = Column(Float)

# # Reflect an existing database into a new model
# Base = automap_base()

# # Reflect the tables
# Base.prepare(engine, reflect=True)

# # Save reference to the table
# Earthquake = Base.classes.seismic_data
# Relief = Base.classes.relief_expenses
# Quaker = Base.classes.quakers2shakers

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# pickled model
model = pickle.load(open('pickle_model.pkl', 'rb'))

#################################################
# Flask Routes
#################################################
@app.route("/")
def home1():
    return render_template("index.html")

@app.route("/home")
def home2():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("vizDashboard.html")

@app.route("/playground")
def playground():
    return render_template("earthquakePlayground.html")

@app.route("/predict", methods=['GET', 'POST'])
def predict():

    input_list = []

    if request.method == 'POST':

        magnitude = request.form.get('magnitude')
        print(magnitude)
        input_list.append(magnitude)

        depth = request.form.get('depth')
        print(depth)
        input_list.append(depth)

        distance = request.form.get('distance')
        print(distance)
        input_list.append(distance)

        azimuthal = request.form.get('azimuthal')
        print(azimuthal)
        input_list.append(azimuthal)

        root_mean = request.form.get('root_mean')
        print(root_mean)
        input_list.append(root_mean)

        print(input_list)

        input_array = [np.array(input_list)]

        print(input_array)

        prediction = model.predict(input_array)[0].upper()

    return render_template("earthquakePlayground.html", test_prediction = prediction) 

@app.route("/machinelearning")
def machinelearning():
    return render_template("machineLearning.html")

@app.route("/routes")
def routes(): 
    print("Server access home")
    return(
        f"project 2: earthquake data API<br>"
        f"Available routes:<br>"
        f"/api/v1.0/earthquake_data<br>"
        f"/api/v1.0/relief_data<br>"
        f"/api/v2.0/quake_data<br>"
        f"/api/v1.0/county_data"
    )

@app.route("/api/v1.0/earthquake_data")
def earthquakes():
    print("Server access earthquake data")
    s = Session(bind=engine)

    results = s.query(earthquake.id, earthquake.Latitude, earthquake.Longitude, earthquake.Depth,
    earthquake.Magnitude, earthquake.Waveform, earthquake.Place, earthquake.Time, earthquake.Type
    ).all()

    s.close()

    earthquake_data = []
    for id, Latitude, Longitude, Depth, Magnitude, Waveform, Place, Time, Type in results:
        earthquake_dict = {}
        earthquake_dict["id"] = id
        earthquake_dict["Latitude"] = Latitude
        earthquake_dict["Longitude"] = Longitude
        earthquake_dict["Depth"] = Depth
        earthquake_dict["Magnitude"] = Magnitude
        earthquake_dict["Waveform"] = Waveform
        earthquake_dict["Place"] = Place
        earthquake_dict["Time"] = Time
        earthquake_dict["Type"] = Type
        earthquake_data.append(earthquake_dict)

    return jsonify(earthquake_data)

@app.route("/api/v1.0/relief_data")
def earthquake_relief():
    print("Server access relief data")
    s = Session(bind=engine)

    results = s.query(uncerf.id, uncerf.Country, uncerf.Total_relief
    ).all()

    s.close()

    relief_data = []
    for id, Country, Total_relief in results:
        relief_dict = {}
        relief_dict["id"] = id
        relief_dict["Country"] = Country
        relief_dict["Total_relief"] = Total_relief
        relief_data.append(relief_dict)

    return jsonify(relief_data)

@app.route("/api/v2.0/quake_data")
def quakers():
    print("Server access quake data")
    s = Session(bind=engine)

    results = s.query(quake.id, quake.country, quake.magnitude, quake.pop_mil, quake.aid_usd_mil,
    quake.earthqks_year_prev)

    s.close()

    quake_data = []
    for id, country, magnitude, pop_mil, aid_us_mil, earthqks_year_prev in results:
        quake_dict = {}
        quake_dict["id"] = id
        quake_dict["country"] = country
        quake_dict["magnitude"] = magnitude
        quake_dict["pop_mil"] = pop_mil
        quake_dict["aid_us_mil"] = aid_us_mil
        quake_dict["earthqks_year_prev"] = earthqks_year_prev
        quake_data.append(quake_dict)

    return jsonify(quake_data)

@app.route("/api/v1.0/county_data")
def county():
    print("Server access county data")
    s = Session(bind=engine)

    results = s.query(county_data.id, county_data.county, county_data.total_damaging_events, county_data.rate_of_damaging_events, county_data.frequency_of_section_1,
    county_data.recurance_interval_1, county_data.area_of_section_1, county_data.frequency_of_section_2, county_data.recurance_interval_2, county_data.area_of_section_2,
    county_data.probability, county_data.latitude, county_data.longitude, county_data.radius)

    s.close()

    county_data_list = []
    for id, county, total_damaging_events, rate_of_damaging_events, frequency_of_section_1, recurance_interval_1, area_of_section_1, frequency_of_section_2, recurance_interval_2, area_of_section_2, probability, latitude, longitude, radius in results:
        county_data_dict = {}
        county_data_dict["id"] = id
        county_data_dict["county"] = county
        county_data_dict["total_damaging_events"] = total_damaging_events
        county_data_dict["rate_of_damaging_events"] = rate_of_damaging_events
        county_data_dict["frequency_of_section_1"] = frequency_of_section_1
        county_data_dict["recurance_interval_1"] = recurance_interval_1
        county_data_dict["area_of_section_1"] = area_of_section_1
        county_data_dict["frequency_of_section_2"] = frequency_of_section_2
        county_data_dict["recurance_interval_2"] = recurance_interval_2
        county_data_dict["area_of_section_2"] = area_of_section_2
        county_data_dict["probability"] = probability
        county_data_dict["latitude"] = latitude
        county_data_dict["longitude"] = longitude
        county_data_dict["radius"] = radius
        county_data_list.append(county_data_dict)
    
    return jsonify(county_data_list)

@app.route("/api/v1.0/county10_data")
def county10():
    print("Server access top 10 county data")
    s = Session(bind=engine)

    results = s.query(county10_data.id, county10_data.county, county10_data.total_damaging_events)

    s.close()

    county10_data_list = []
    for id, county, total_damaging_events in results:
        county10_data_dict = {}
        county10_data_dict["id"] = id
        county10_data_dict["county"] = county
        county10_data_dict["total_damaging_events"] = total_damaging_events
        county10_data_list.append(county10_data_dict)
    
    return jsonify(county10_data_list)

if __name__=="__main__":
    app.run(debug = True)