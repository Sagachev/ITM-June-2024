import pandas as pd
import matplotlib.pyplot as plt

bikes = pd.read_csv('bikes.csv')
bikes['Berri 1'].plot()
plt.show()