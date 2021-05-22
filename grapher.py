


import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

waveform_per = pd.read_csv("data/ml/stats/Waveformtotals.csv")
waveform_labels = waveform_per["Waveforms"]
waveform_data = waveform_per["Count"]
waveform_percent = (waveform_per["Count"]/waveform_data.sum())*100
# explode = [.5,.25,.25,-.5,0,0,0,0,0]

pieplot = plt.pie(x=waveform_data,labels=waveform_labels, radius=1.1, autopct="%1.1f%%")
plt.savefig("data/visualizations/Percentage_of_Total_Waveform_Pie_Chart.png", )
plt.show()


predicition_data = pd.read_csv("data/ml/stats/PredictionData.csv")

trueDF = predicition_data.loc[predicition_data["Match"] == True]
falseDF = predicition_data.loc[predicition_data["Match"] == False]





truey = trueDF["Depth"]
truex = trueDF["Magnitude"]

falsey = falseDF["Depth"]
falsex = falseDF["Magnitude"]


colors = ['red','green','blue','purple', 'yellow', 'magenta', 'black', 'brown', 'cyan']

# setup the figure
fig, (ax, ax1) = plt.subplots(nrows=2, figsize=(10,10))

ax.scatter(truex, truey, c="green")
ax.set_ylabel("Depth")
ax.set_xlabel("Magnitude")
ax.set_title("Correct Predictions Depth vs. Magnitude")
ax1.scatter(falsex,falsey, marker="x", c="red")
ax1.set_ylabel("Depth")
ax1.set_xlabel("Magnitude")
ax1.set_title("Incorrect Predictions Depth vs. Magnitude")
plt.savefig("data/visualizations/Correct_vs_Incorrect_Over_Depth_and_Magnitude.png")
plt.show()

probability = [75, 72, 65, 82, 56]
insurance = [2100, 1500, 3000, 1200, 7500]

label = ["LA", "San Bernardino", "SF", "Inyo", "Ventura"]

plt.scatter(x=insurance, y=probability)
plt.show()