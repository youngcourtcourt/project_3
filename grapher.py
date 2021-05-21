import matplotlib.pyplot  as plt


probability = [75, 72, 65, 82, 56]
insurance = [2100, 1500, 3000, 1200, 7500]

label = ["LA", "San Bernardino", "SF", "Inyo", "Ventura"]

plt.scatter(x=insurance, y=probability)
plt.show()