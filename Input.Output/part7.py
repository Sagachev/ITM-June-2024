import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

plt.rcParams['figure.figsize'] = (10, 5)
complaints = pd.read_csv('bikes.csv')
complaints[:5]
print(complaints)
