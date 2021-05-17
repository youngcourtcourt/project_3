
import requests
import pandas as pd
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import ComplementNB
from sklearn.svm import SVC
from sklearn import metrics
import math
from datetime import datetime
from datetime import timedelta
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from pprint import pprint
data_url  = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-1-01&endtime=2014-1-07&eventtype=earthquake&limit=20000" \
            "&maxlatitude=41.9961351764005&minlongitude=-124.21129087870494&minlatitude=32.76271062703306&maxlongitude=-114.51377843459622"

alameda_county = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-1-01&endtime=2014-3-01&eventtype=earthquake&limit=20000" \
            "&latitude=37.80483&longitude=-122.27248&maxradiuskm=956"

alpine_county = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-1-01&endtime=2014-3-01&eventtype=earthquake&limit=20000" \
            "&latitude=38.69356&longitude=-119.777756&maxradiuskm=957"

amador_county = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-1-01&endtime=2014-3-01&eventtype=earthquake&limit=20000" \
            "&latitude=38.44585&longitude=-120.65244&maxradiuskm=785"

butte_county = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-1-01&endtime=2014-3-01&eventtype=earthquake&limit=20000" \
            "&latitude=39.51234&longitude=-121.55461&maxradiuskm=957"

# 37.80483° N, -122.27248° E

california_weekly = requests.get(data_url)
alameda_quarterly = requests.get(alameda_county)
alpine_quarterly = requests.get(alpine_county)
amador_quarterly = requests.get(amador_county)
alpine_quarterly = requests.get(alpine_county)
# LA_weekly

data = california_weekly.json()
alameda_quarterly_data = alameda_quarterly.json()
alpine_quarterly_data = alpine_quarterly.json()
amador_quarterly_data = amador_quarterly.json()
alpine_quarterly_data = alpine_quarterly.json()
alpine_quarterly_data = alpine_quarterly.json()




dmin = []
tsunami = []
mag = []
magType = []
gap = []
rms = []
sig = []
none = []
depth = []
# pprint(data)

#wrapper to extract data from GEOJson
for x in data["features"]:
    if x["properties"]["dmin"] == None:
        none.append((x["properties"]["dmin"]))
    else:
        dmin.append(x["properties"]["dmin"])


for x in data["features"]:
    if x["properties"]["mag"] == None:
        none.append((x["properties"]["mag"]))
    else:
        mag.append(x["properties"]["mag"])


for x in data["features"]:
    if x["properties"]["magType"] == None:
        none.append((x["properties"]["magType"]))
    else:
        magType.append(x["properties"]["magType"])


for x in data["features"]:
    if x["properties"]["gap"] == None:
        none.append((x["properties"]["gap"]))
    else:
        gap.append(x["properties"]["gap"])


for x in data["features"]:
    if x["properties"]["rms"] == None:
        none.append((x["properties"]["rms"]))
    else:
        rms.append(x["properties"]["rms"])


for x in data["features"]:
        depth.append(x["geometry"]["coordinates"][2])

stateDF = pd.DataFrame(list(zip(depth, dmin, rms, gap, mag, magType)), columns=["Depth","Distance to Epicenter","Root Mean Square","Azimuthal Gap","Magnitude", "Waveform"])



state_weekly_totals = stateDF.count().max()
state_weekly_average = state_weekly_totals/7





dmin = []
tsunami = []
mag = []
magType = []
gap = []
rms = []
sig = []
none = []
depth = []

#alpine county
for x in alpine_quarterly_data["features"]:
    if x["properties"]["dmin"] == None:
        none.append((x["properties"]["dmin"]))
    else:
        dmin.append(x["properties"]["dmin"])
    if x["properties"]["mag"] == None:
        none.append((x["properties"]["mag"]))
    else:
        mag.append(x["properties"]["mag"])
    if x["properties"]["magType"] == None:
        none.append((x["properties"]["magType"]))
    else:
        magType.append(x["properties"]["magType"])

    if x["properties"]["gap"] == None:
        none.append((x["properties"]["gap"]))
    else:
        gap.append(x["properties"]["gap"])

    if x["properties"]["rms"] == None:
        none.append((x["properties"]["rms"]))
    else:
        rms.append(x["properties"]["rms"])

        depth.append(x["geometry"]["coordinates"][2])


alpineDF = pd.DataFrame(list(zip(depth, dmin, rms, gap, mag, magType)), columns=["Depth","Distance to Epicenter","Root Mean Square","Azimuthal Gap","Magnitude", "Waveform"])

print(alpineDF)

alpine_yearly_totals = alpineDF.count().max()
alpine_yearly_totals = alpine_yearly_totals*4
alpine_daily_average = alpine_yearly_totals/365
print(alpine_daily_average)



dmin = []
tsunami = []
mag = []
magType = []
gap = []
rms = []
sig = []
none = []
depth = []

county_data = pd.read_csv("data/county_data.csv")
for x in range(len(county_data)):

    latitude = county_data["Latitude"]

    longitude = county_data["Longitude"]
    radius = county_data["Radius"]
    name = county_data["County Name"]

    latitude = latitude[x]
    longitude = longitude[x]
    radius = radius[x]
    radius = math.sqrt(radius)
    name = name[x]


    county = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-1-01&endtime=2014-3-01&eventtype=earthquake&limit=20000" \
                     f"&latitude={latitude}&longitude={longitude}&maxradiuskm={radius}"


    request = requests.get(county)
    response = request.json()

    dmin = []
    tsunami = []
    mag = []
    magType = []
    gap = []
    rms = []
    sig = []
    none = []
    depth = []

    # extracts data
    for x in response["features"]:
        if x["properties"]["dmin"] == None:
            none.append((x["properties"]["dmin"]))
        else:
            dmin.append(x["properties"]["dmin"])
        if x["properties"]["mag"] == None:
            none.append((x["properties"]["mag"]))
        else:
            mag.append(x["properties"]["mag"])
        if x["properties"]["magType"] == None:
            none.append((x["properties"]["magType"]))
        else:
            magType.append(x["properties"]["magType"])

        if x["properties"]["gap"] == None:
            none.append((x["properties"]["gap"]))
        else:
            gap.append(x["properties"]["gap"])

        if x["properties"]["rms"] == None:
            none.append((x["properties"]["rms"]))
        else:
            rms.append(x["properties"]["rms"])

        depth.append(x["geometry"]["coordinates"][2])


    infoDF = pd.DataFrame(list(zip(depth, dmin, rms, gap, mag, magType)),
                            columns=["Depth", "Distance to Epicenter", "Root Mean Square", "Azimuthal Gap",
                                      "Magnitude", "Waveform"])

    infoDF.to_csv(f"data/county_data/{name}")

    #
    # alameda_yearly_totals = alamedaDF.count().max()
    # alameda_yearly_totals = alameda_yearly_totals * 4
    # alameda_daily_average = alameda_yearly_totals / 365
i=0
holder=0
Holder_df = pd.DataFrame()
for x in range(len(county_data)):
    year1 = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
    year2 = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
    year1 = year1[i]
    year2 = year2[i]
    dmin = []
    time = []
    mag = []
    magType = []
    gap = []
    rms = []
    sig = []
    none = []
    depth = []

    latitude = county_data["Latitude"]
    longitude = county_data["Longitude"]
    radius = county_data["Radius"]
    name = county_data["County Name"]

    latitude = latitude[x]
    longitude = longitude[x]
    radius = radius[x]
    radius2 = math.sqrt(radius)
    name = name[x]


    county = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2010-1-01&endtime=2011-1-01&eventtype=earthquake&limit=20000" \
             f"&latitude={latitude}&longitude={longitude}&maxradiuskm={radius2}&minmagnitude=5.0"
    county1 = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2011-1-01&endtime=2012-1-01&eventtype=earthquake&limit=20000" \
             f"&latitude={latitude}&longitude={longitude}&maxradiuskm={radius2}&minmagnitude=5.0"
    county2 = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2012-1-01&endtime=2013-1-01&eventtype=earthquake&limit=20000" \
             f"&latitude={latitude}&longitude={longitude}&maxradiuskm={radius2}&minmagnitude=5.0"
    county3 = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2013-1-01&endtime=2014-1-01&eventtype=earthquake&limit=20000" \
             f"&latitude={latitude}&longitude={longitude}&maxradiuskm={radius2}&minmagnitude=5.0"
    county4 = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-1-01&endtime=2015-1-01&eventtype=earthquake&limit=20000" \
             f"&latitude={latitude}&longitude={longitude}&maxradiuskm={radius2}&minmagnitude=5.0"
    county5 = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2015-1-01&endtime=2016-1-01&eventtype=earthquake&limit=20000" \
             f"&latitude={latitude}&longitude={longitude}&maxradiuskm={radius2}&minmagnitude=5.0"
    county6 = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2016-1-01&endtime=2017-1-01&eventtype=earthquake&limit=20000" \
             f"&latitude={latitude}&longitude={longitude}&maxradiuskm={radius2}&minmagnitude=5.0"
    county7 = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2017-1-01&endtime=2018-1-01&eventtype=earthquake&limit=20000" \
             f"&latitude={latitude}&longitude={longitude}&maxradiuskm={radius2}&minmagnitude=5.0"
    county8 = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2018-1-01&endtime=2019-1-01&eventtype=earthquake&limit=20000" \
             f"&latitude={latitude}&longitude={longitude}&maxradiuskm={radius2}&minmagnitude=5.0"


    request = requests.get(county)
    request1 = requests.get(county1)
    request2 = requests.get(county2)
    request3 = requests.get(county3)
    request4 = requests.get(county4)
    request5 = requests.get(county5)
    request6 = requests.get(county6)
    request7 = requests.get(county7)
    request8 = requests.get(county8)





    response = request.json()
    response1 = request.json()
    response2 = request.json()
    response3 = request.json()
    response4 = request.json()
    response5 = request.json()
    response6 = request.json()
    response7 = request.json()
    response8 = request.json()
    response_list = [response, response1, response2, response3, response4, response5, response6, response7, response8]
    # for y in response_list:
    for x in response["features"]:
        if x["properties"]["dmin"] == None:
            none.append((x["properties"]["dmin"]))
        else:
            dmin.append(x["properties"]["dmin"])
        if x["properties"]["mag"] == None:
            none.append((x["properties"]["mag"]))
        else:
            mag.append(x["properties"]["mag"])
        if x["properties"]["magType"] == None:
            none.append((x["properties"]["magType"]))
        else:
            magType.append(x["properties"]["magType"])

        if x["properties"]["gap"] == None:
            none.append((x["properties"]["gap"]))
        else:
            gap.append(x["properties"]["gap"])

        if x["properties"]["rms"] == None:
                none.append((x["properties"]["rms"]))
        else:
            rms.append(x["properties"]["rms"])
        time.append(x["properties"]["time"])
        depth.append(x["geometry"]["coordinates"][2])

    for x in response1["features"]:
        if x["properties"]["dmin"] == None:
            none.append((x["properties"]["dmin"]))
        else:
            dmin.append(x["properties"]["dmin"])
        if x["properties"]["mag"] == None:
            none.append((x["properties"]["mag"]))
        else:
            mag.append(x["properties"]["mag"])
        if x["properties"]["magType"] == None:
            none.append((x["properties"]["magType"]))
        else:
            magType.append(x["properties"]["magType"])

        if x["properties"]["gap"] == None:
            none.append((x["properties"]["gap"]))
        else:
            gap.append(x["properties"]["gap"])

        if x["properties"]["rms"] == None:
            none.append((x["properties"]["rms"]))
        else:
            rms.append(x["properties"]["rms"])
        time.append(x["properties"]["time"])
        depth.append(x["geometry"]["coordinates"][2])

    for x in response2["features"]:
        if x["properties"]["dmin"] == None:
            none.append((x["properties"]["dmin"]))
        else:
            dmin.append(x["properties"]["dmin"])
        if x["properties"]["mag"] == None:
            none.append((x["properties"]["mag"]))
        else:
            mag.append(x["properties"]["mag"])
        if x["properties"]["magType"] == None:
            none.append((x["properties"]["magType"]))
        else:
            magType.append(x["properties"]["magType"])

        if x["properties"]["gap"] == None:
            none.append((x["properties"]["gap"]))
        else:
            gap.append(x["properties"]["gap"])

        if x["properties"]["rms"] == None:
            none.append((x["properties"]["rms"]))
        else:
            rms.append(x["properties"]["rms"])
        time.append(x["properties"]["time"])
        depth.append(x["geometry"]["coordinates"][2])

    for x in response3["features"]:
        if x["properties"]["dmin"] == None:
            none.append((x["properties"]["dmin"]))
        else:
            dmin.append(x["properties"]["dmin"])
        if x["properties"]["mag"] == None:
            none.append((x["properties"]["mag"]))
        else:
            mag.append(x["properties"]["mag"])
        if x["properties"]["magType"] == None:
            none.append((x["properties"]["magType"]))
        else:
            magType.append(x["properties"]["magType"])

        if x["properties"]["gap"] == None:
            none.append((x["properties"]["gap"]))
        else:
            gap.append(x["properties"]["gap"])

        if x["properties"]["rms"] == None:
            none.append((x["properties"]["rms"]))
        else:
            rms.append(x["properties"]["rms"])
        time.append(x["properties"]["time"])
        depth.append(x["geometry"]["coordinates"][2])

    for x in response4["features"]:
        if x["properties"]["dmin"] == None:
            none.append((x["properties"]["dmin"]))
        else:
            dmin.append(x["properties"]["dmin"])
        if x["properties"]["mag"] == None:
            none.append((x["properties"]["mag"]))
        else:
            mag.append(x["properties"]["mag"])
        if x["properties"]["magType"] == None:
            none.append((x["properties"]["magType"]))
        else:
            magType.append(x["properties"]["magType"])

        if x["properties"]["gap"] == None:
            none.append((x["properties"]["gap"]))
        else:
            gap.append(x["properties"]["gap"])

        if x["properties"]["rms"] == None:
            none.append((x["properties"]["rms"]))
        else:
            rms.append(x["properties"]["rms"])
        time.append(x["properties"]["time"])
        depth.append(x["geometry"]["coordinates"][2])

    for x in response5["features"]:
        if x["properties"]["dmin"] == None:
            none.append((x["properties"]["dmin"]))
        else:
            dmin.append(x["properties"]["dmin"])
        if x["properties"]["mag"] == None:
            none.append((x["properties"]["mag"]))
        else:
            mag.append(x["properties"]["mag"])
        if x["properties"]["magType"] == None:
            none.append((x["properties"]["magType"]))
        else:
            magType.append(x["properties"]["magType"])

        if x["properties"]["gap"] == None:
            none.append((x["properties"]["gap"]))
        else:
            gap.append(x["properties"]["gap"])

        if x["properties"]["rms"] == None:
            none.append((x["properties"]["rms"]))
        else:
            rms.append(x["properties"]["rms"])
        time.append(x["properties"]["time"])
        depth.append(x["geometry"]["coordinates"][2])

    for x in response6["features"]:
        if x["properties"]["dmin"] == None:
            none.append((x["properties"]["dmin"]))
        else:
            dmin.append(x["properties"]["dmin"])
        if x["properties"]["mag"] == None:
            none.append((x["properties"]["mag"]))
        else:
            mag.append(x["properties"]["mag"])
        if x["properties"]["magType"] == None:
            none.append((x["properties"]["magType"]))
        else:
            magType.append(x["properties"]["magType"])

        if x["properties"]["gap"] == None:
            none.append((x["properties"]["gap"]))
        else:
            gap.append(x["properties"]["gap"])

        if x["properties"]["rms"] == None:
            none.append((x["properties"]["rms"]))
        else:
            rms.append(x["properties"]["rms"])
        time.append(x["properties"]["time"])
        depth.append(x["geometry"]["coordinates"][2])

    for x in response7["features"]:
        if x["properties"]["dmin"] == None:
            none.append((x["properties"]["dmin"]))
        else:
            dmin.append(x["properties"]["dmin"])
        if x["properties"]["mag"] == None:
            none.append((x["properties"]["mag"]))
        else:
            mag.append(x["properties"]["mag"])
        if x["properties"]["magType"] == None:
            none.append((x["properties"]["magType"]))
        else:
            magType.append(x["properties"]["magType"])

        if x["properties"]["gap"] == None:
            none.append((x["properties"]["gap"]))
        else:
            gap.append(x["properties"]["gap"])

        if x["properties"]["rms"] == None:
            none.append((x["properties"]["rms"]))
        else:
            rms.append(x["properties"]["rms"])
        time.append(x["properties"]["time"])
        depth.append(x["geometry"]["coordinates"][2])

    for x in response8["features"]:
        if x["properties"]["dmin"] == None:
            none.append((x["properties"]["dmin"]))
        else:
            dmin.append(x["properties"]["dmin"])
        if x["properties"]["mag"] == None:
            none.append((x["properties"]["mag"]))
        else:
            mag.append(x["properties"]["mag"])
        if x["properties"]["magType"] == None:
            none.append((x["properties"]["magType"]))
        else:
            magType.append(x["properties"]["magType"])

        if x["properties"]["gap"] == None:
            none.append((x["properties"]["gap"]))
        else:
            gap.append(x["properties"]["gap"])

        if x["properties"]["rms"] == None:
            none.append((x["properties"]["rms"]))
        else:
            rms.append(x["properties"]["rms"])
        time.append(x["properties"]["time"])
        depth.append(x["geometry"]["coordinates"][2])


    infoDF = pd.DataFrame(list(zip(time, depth, dmin, rms, gap, mag, magType)),
                            columns=["Time", "Depth", "Distance to Epicenter", "Root Mean Square", "Azimuthal Gap",
                                      "Magnitude", "Waveform"])
    infoDF.to_csv(f"data/mag5.0data/{name}")
    # Holder_df = Holder_df.merge(infoDF, "inner", right_index=True, left_index=True)
    #     Holder_df.to_csv(f"mag5.0data/{name}")
    #
















