import requests
import pandas as pd
from sklearn.naive_bayes import BaseDiscreteNB
from sklearn.naive_bayes import ComplementNB
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import time
import math
from pprint import pprint

#
#
#
# dmin = []
# time = []
# mag = []
# magType = []
# gap = []
# rms = []
# sig = []
# none = []
# depth = []
#
#
#
#
# county = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2010-1-01&endtime=2011-1-01&eventtype=earthquake&limit=20000" \
#              f"&maxlatitude=41.9961351764005&minlongitude=-124.21129087870494&minlatitude=32.76271062703306&maxlongitude=-114.51377843459622&maxmagnitude=3.9" \
#
# county1 = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2011-1-01&endtime=2012-1-01&eventtype=earthquake&limit=20000" \
#              f"&maxlatitude=41.9961351764005&minlongitude=-124.21129087870494&minlatitude=32.76271062703306&maxlongitude=-114.51377843459622&minmagnitude=3.9"
# county2 = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2012-1-01&endtime=2013-1-01&eventtype=earthquake&limit=20000" \
#              f"&maxlatitude=41.9961351764005&minlongitude=-124.21129087870494&minlatitude=32.76271062703306&maxlongitude=-114.51377843459622&minmagnitude=5.0"
# county3 = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2013-1-01&endtime=2014-1-01&eventtype=earthquake&limit=20000" \
#              f"&maxlatitude=41.9961351764005&minlongitude=-124.21129087870494&minlatitude=32.76271062703306&maxlongitude=-114.51377843459622  "
# county4 = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-1-01&endtime=2015-1-01&eventtype=earthquake&limit=20000" \
#              f"&maxlatitude=41.9961351764005&minlongitude=-124.21129087870494&minlatitude=32.76271062703306&maxlongitude=-114.51377843459622&minmagnitude=3.9"
# county5 = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2015-1-01&endtime=2016-1-01&eventtype=earthquake&limit=20000" \
#              f"&maxlatitude=41.9961351764005&minlongitude=-124.21129087870494&minlatitude=32.76271062703306&maxlongitude=-114.51377843459622&minmagnitude=5.0"
# county6 = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2016-1-01&endtime=2017-1-01&eventtype=earthquake&limit=20000" \
#              f"&maxlatitude=41.9961351764005&minlongitude=-124.21129087870494&minlatitude=32.76271062703306&maxlongitude=-114.51377843459622"
# county7 = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2017-1-01&endtime=2018-1-01&eventtype=earthquake&limit=20000" \
#              f"&maxlatitude=41.9961351764005&minlongitude=-124.21129087870494&minlatitude=32.76271062703306&maxlongitude=-114.51377843459622&minmagnitude=3.9"
# county8 = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2018-1-01&endtime=2019-1-01&eventtype=earthquake&limit=20000" \
#              f"&maxlatitude=41.9961351764005&minlongitude=-124.21129087870494&minlatitude=32.76271062703306&maxlongitude=-114.51377843459622&minmagnitude=5.0"
#
#
# request = requests.get(county)
# request1 = requests.get(county1)
# request2 = requests.get(county2)
# request3 = requests.get(county3)
# request4 = requests.get(county4)
# request5 = requests.get(county5)
# request6 = requests.get(county6)
# request7 = requests.get(county7)
# request8 = requests.get(county8)
#
#
#
#
#
# response = request.json()
# response1 = request1.json()
# response2 = request2.json()
# response3 = request3.json()
# response4 = request4.json()
# response5 = request5.json()
# response6 = request6.json()
# response7 = request7.json()
# response8 = request8.json()
#
# print(response7)
# response_list = [response, response1, response2, response3, response4, response5, response6, response7, response8]
#     # for y in response_list:
# for x in response["features"]:
#     if x["properties"]["dmin"] == None:
#         none.append((x["properties"]["dmin"]))
#     else:
#         dmin.append(x["properties"]["dmin"])
#     if x["properties"]["mag"] == None:
#         none.append((x["properties"]["mag"]))
#     else:
#         mag.append(x["properties"]["mag"])
#     if x["properties"]["magType"] == None:
#         none.append((x["properties"]["magType"]))
#     else:
#         magType.append(x["properties"]["magType"])
#
#     if x["properties"]["gap"] == None:
#         none.append((x["properties"]["gap"]))
#     else:
#         gap.append(x["properties"]["gap"])
#
#     if x["properties"]["rms"] == None:
#         none.append((x["properties"]["rms"]))
#     else:
#         rms.append(x["properties"]["rms"])
#     time.append(x["properties"]["time"])
#     depth.append(x["geometry"]["coordinates"][2])
#
#
# for x in response1["features"]:
#     if x["properties"]["dmin"] == None:
#         none.append((x["properties"]["dmin"]))
#     else:
#         dmin.append(x["properties"]["dmin"])
#     if x["properties"]["mag"] == None:
#         none.append((x["properties"]["mag"]))
#     else:
#         mag.append(x["properties"]["mag"])
#     if x["properties"]["magType"] == None:
#         none.append((x["properties"]["magType"]))
#     else:
#         magType.append(x["properties"]["magType"])
#
#     if x["properties"]["gap"] == None:
#         none.append((x["properties"]["gap"]))
#     else:
#         gap.append(x["properties"]["gap"])
#
#     if x["properties"]["rms"] == None:
#         none.append((x["properties"]["rms"]))
#     else:
#         rms.append(x["properties"]["rms"])
#     time.append(x["properties"]["time"])
#     depth.append(x["geometry"]["coordinates"][2])
#
#     for x in response2["features"]:
#         if x["properties"]["dmin"] == None:
#             none.append((x["properties"]["dmin"]))
#         else:
#             dmin.append(x["properties"]["dmin"])
#         if x["properties"]["mag"] == None:
#             none.append((x["properties"]["mag"]))
#         else:
#             mag.append(x["properties"]["mag"])
#         if x["properties"]["magType"] == None:
#             none.append((x["properties"]["magType"]))
#         else:
#             magType.append(x["properties"]["magType"])
#
#         if x["properties"]["gap"] == None:
#             none.append((x["properties"]["gap"]))
#         else:
#             gap.append(x["properties"]["gap"])
#
#         if x["properties"]["rms"] == None:
#             none.append((x["properties"]["rms"]))
#         else:
#             rms.append(x["properties"]["rms"])
#         time.append(x["properties"]["time"])
#         depth.append(x["geometry"]["coordinates"][2])
#
# for x in response3["features"]:
#     if x["properties"]["dmin"] == None:
#         none.append((x["properties"]["dmin"]))
#     else:
#         dmin.append(x["properties"]["dmin"])
#     if x["properties"]["mag"] == None:
#         none.append((x["properties"]["mag"]))
#     else:
#         mag.append(x["properties"]["mag"])
#     if x["properties"]["magType"] == None:
#         none.append((x["properties"]["magType"]))
#     else:
#         magType.append(x["properties"]["magType"])
#
#     if x["properties"]["gap"] == None:
#         none.append((x["properties"]["gap"]))
#     else:
#         gap.append(x["properties"]["gap"])
#
#     if x["properties"]["rms"] == None:
#         none.append((x["properties"]["rms"]))
#     else:
#         rms.append(x["properties"]["rms"])
#     time.append(x["properties"]["time"])
#     depth.append(x["geometry"]["coordinates"][2])
#
# for x in response4["features"]:
#     if x["properties"]["dmin"] == None:
#         none.append((x["properties"]["dmin"]))
#     else:
#         dmin.append(x["properties"]["dmin"])
#     if x["properties"]["mag"] == None:
#         none.append((x["properties"]["mag"]))
#     else:
#         mag.append(x["properties"]["mag"])
#     if x["properties"]["magType"] == None:
#         none.append((x["properties"]["magType"]))
#     else:
#         magType.append(x["properties"]["magType"])
#
#     if x["properties"]["gap"] == None:
#         none.append((x["properties"]["gap"]))
#     else:
#         gap.append(x["properties"]["gap"])
#
#     if x["properties"]["rms"] == None:
#         none.append((x["properties"]["rms"]))
#     else:
#         rms.append(x["properties"]["rms"])
#     time.append(x["properties"]["time"])
#     depth.append(x["geometry"]["coordinates"][2])
#
# for x in response5["features"]:
#     if x["properties"]["dmin"] == None:
#         none.append((x["properties"]["dmin"]))
#     else:
#         dmin.append(x["properties"]["dmin"])
#     if x["properties"]["mag"] == None:
#         none.append((x["properties"]["mag"]))
#     else:
#         mag.append(x["properties"]["mag"])
#     if x["properties"]["magType"] == None:
#         none.append((x["properties"]["magType"]))
#     else:
#         magType.append(x["properties"]["magType"])
#
#     if x["properties"]["gap"] == None:
#         none.append((x["properties"]["gap"]))
#     else:
#         gap.append(x["properties"]["gap"])
#
#     if x["properties"]["rms"] == None:
#         none.append((x["properties"]["rms"]))
#     else:
#         rms.append(x["properties"]["rms"])
#     time.append(x["properties"]["time"])
#     depth.append(x["geometry"]["coordinates"][2])
#
# for x in response6["features"]:
#     if x["properties"]["dmin"] == None:
#         none.append((x["properties"]["dmin"]))
#     else:
#         dmin.append(x["properties"]["dmin"])
#     if x["properties"]["mag"] == None:
#         none.append((x["properties"]["mag"]))
#     else:
#         mag.append(x["properties"]["mag"])
#     if x["properties"]["magType"] == None:
#         none.append((x["properties"]["magType"]))
#     else:
#         magType.append(x["properties"]["magType"])
#
#     if x["properties"]["gap"] == None:
#         none.append((x["properties"]["gap"]))
#     else:
#         gap.append(x["properties"]["gap"])
#
#     if x["properties"]["rms"] == None:
#         none.append((x["properties"]["rms"]))
#     else:
#         rms.append(x["properties"]["rms"])
#     time.append(x["properties"]["time"])
#     depth.append(x["geometry"]["coordinates"][2])
#
# for x in response7["features"]:
#     if x["properties"]["dmin"] == None:
#         none.append((x["properties"]["dmin"]))
#     else:
#         dmin.append(x["properties"]["dmin"])
#     if x["properties"]["mag"] == None:
#         none.append((x["properties"]["mag"]))
#     else:
#         mag.append(x["properties"]["mag"])
#     if x["properties"]["magType"] == None:
#         none.append((x["properties"]["magType"]))
#     else:
#         magType.append(x["properties"]["magType"])
#
#     if x["properties"]["gap"] == None:
#         none.append((x["properties"]["gap"]))
#     else:
#         gap.append(x["properties"]["gap"])
#
#     if x["properties"]["rms"] == None:
#         none.append((x["properties"]["rms"]))
#     else:
#         rms.append(x["properties"]["rms"])
#     time.append(x["properties"]["time"])
#     depth.append(x["geometry"]["coordinates"][2])
#
#
# for x in response8["features"]:
#     if x["properties"]["dmin"] == None:
#         none.append((x["properties"]["dmin"]))
#     else:
#         dmin.append(x["properties"]["dmin"])
#     if x["properties"]["mag"] == None:
#         none.append((x["properties"]["mag"]))
#     else:
#         mag.append(x["properties"]["mag"])
#     if x["properties"]["magType"] == None:
#         none.append((x["properties"]["magType"]))
#     else:
#         magType.append(x["properties"]["magType"])
#
#     if x["properties"]["gap"] == None:
#         none.append((x["properties"]["gap"]))
#     else:
#         gap.append(x["properties"]["gap"])
#
#     if x["properties"]["rms"] == None:
#         none.append((x["properties"]["rms"]))
#     else:
#         rms.append(x["properties"]["rms"])
#     time.append(x["properties"]["time"])
#     depth.append(x["geometry"]["coordinates"][2])
#
#
# case_sensitive_Waveforms = []
# for x in magType:
#    case_sensitive_Waveforms.append(x.lower())
#
# infoDF2 = pd.DataFrame(list(zip(time, depth, dmin, rms, gap, mag, case_sensitive_Waveforms)),
#                         columns=["Time", "Depth", "Distance", "Root Mean Square", "Azimuthal Gap",
#                                        "Magnitude", "Waveform"])
# # magdf = pd.DataFrame({"Magnitude":mag})
# # magdf = magdf.abs()
# # infoDF2.merge(magdf, "inner", left_index=True, right_index=True)
# print(infoDF2)
# infoDF2.to_csv(f"data/ml/input/trainer.csv")
# case_sensitive_Waveforms = pd.DataFrame(case_sensitive_Waveforms)


Ses_DF = pd.read_csv("data/ml/input/trainer.csv")

Waveformtotals = Ses_DF["Waveform"]

case_sensitive_Waveforms = []
for x in Waveformtotals:
   case_sensitive_Waveforms.append(x.lower())
Waveformtotals = pd.DataFrame({"Waveforms":case_sensitive_Waveforms})
Waveformtotals = Waveformtotals.value_counts()
Waveformtotals = Waveformtotals.rename("Count")
Waveformtotals.to_csv(path_or_buf="data/ml/stats/Waveformtotals.csv")

Ses_DF["Magnitude"] = Ses_DF["Magnitude"].abs()
Ses_DF["Depth"] = Ses_DF["Depth"].abs()


X = Ses_DF[["Magnitude", "Depth", "Distance to Epicenter", "Azimuthal Gap", "Root Mean Square"]]
y = Ses_DF["Waveform"]

# test train split
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.1)
# model creation
clf = SVC()

# fits data
clf.fit(X_train, Y_train)

# scores model
score = clf.score(X_test, Y_test)
print(f"Train Score:{clf.score(X_train,Y_train)}")
print(f"Accuracy of model: {score*100}%")
# predicted model
predictedY = clf.predict(X_test)
predicted = pd.DataFrame({"Predicted_Waveform":predictedY})
print(predicted)
print(Y_test, X_test)


# merges predicted and actual Waveforms
compared = predicted.merge(Y_test, "inner", right_index=True, left_index=True)
compared = compared.reset_index(drop=True)
compared.to_csv(path_or_buf="data/ml/stats/PredictionData.csv")
# print(compared)
# compared accuracy list passes a True if the prediction matches the actual waveform, and False if it doesn't
# i is the index for the while loop
# i_list creates an index within the data for later processing

# PROTOTYPE CODE BELOW! DO NOT TOUCH OR UNCOMMENT!!!!!!!!!!
#-------------------------------------------------------------------------
# YOU HAVE BEEN WARNED !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#--------------------------------------------------------------------------------------

compared_accuracy = []
i = 0
i_list = []
# while loop for passing correct or incorrect predictions
# while i is less then length, so every element gets covered
while i < len(compared):
    # finds the values un compared Dataframe at index i
    value = compared.loc[i]

    # transposes value
    value = value.T
    # assigns actual value to com1 and predicted value to com2
    com1 = value["Waveform"]
    com2 = value["Predicted_Waveform"]
    # compares com to com 2 if same then true if different false then adds 1 to i index
    if com1 == com2:
       compared_accuracy.append("True")
       i_list.append(i)
       i += 1

    elif com1 != com2:
       compared_accuracy.append("False")
       i_list.append(i)
       i += 1
    else:
        compared_accuracy.append("ERROR")
        i_list.append(i)
        i += 1

#creates datafrome from list for accuracy and index list
compared_accuracyDF = pd.DataFrame({"Match": compared_accuracy})
i_listDF = pd.DataFrame({"Index": i_list})
# merges compared with index,accuracy, and magnitude, depth
compared = compared.merge(i_listDF, "inner", right_index=True, left_index=True)
compared = compared.merge(compared_accuracyDF, "inner", right_index=True, left_index=True)
compared = compared.merge(X, "inner", right_index=True, left_index=True)




# writes compared to csv
compared.to_csv(path_or_buf="data/ml/stats/PredictionData.csv")

# creates a Key stats DF with Accurate Predicted Total

# counts number of true and false values
Accurate_Predicted_Total = compared["Match"].value_counts()
# calculates actual/experimental %
Accurate_Predicted_Total["Actual Percentage"] = (Accurate_Predicted_Total["True"]/compared["Index"].max())*100

# grabs theoretical % from score variable above
Accurate_Predicted_Total["Theoretical Percentage"] = score*100
# calculates percent error (actual-theoretical)/theoretical
# NOTE: any value of absolute value should bre read as positive even if negative
Accurate_Predicted_Total["Percent Error"] = (((score*100)-(Accurate_Predicted_Total["True"]/compared["Index"].max())*100)/(score*100))*100
Accurate_Predicted_Total["Percent Error"] = math.fabs(Accurate_Predicted_Total["Percent Error"])
Accurate_Predicted_Total.to_csv(path_or_buf="data/ml/stats/Keystats.csv")

from grapher import graph
graph()



