
import requests
import pandas as pd
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import ComplementNB
from sklearn.svm import SVC
from sklearn import metrics
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
for x in range(len(county_data)):
    year1=[2014, 2015, 2016, 2017, 2018]
    year2 = [2015, 2016, 2017, 2018, 2019]
    year1 = year1[x]
    year2 = year2[x]
    dmin = []
    tsunami = []
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
    name = name[x]


    county = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={year1}-1-01&endtime={year2}-1-01&eventtype=earthquake&limit=20000" \
             f"&latitude={latitude}&longitude={longitude}&maxradiuskm={radius}&minmagnitude=5.0"

    request = requests.get(county)
    response = request.json()
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

        yearly_totals = infoDF.count().max()
        holder = yearly_totals+holder
        i += 1
        if i == 5:
            total = holder
            holder = 0
            rate_mag5 = total/5
            freq_section = rate_mag5*total
            recurrance_interval = 1/freq_section
            area = radius*2
            conditional_interval = (recurrance_interval*area)/area
            key_stats = pd.DataFrame([{"Total Damaging Events": total}, {"Rate of Damaging Events":rate_mag5}, {"Frequncy of Section":freq_section}, {"Reccurance Interval":recurrance_interval}, {"Are of Section":area}])

            key_stats.to_csv(f"data/key_stats_data/{name}")














