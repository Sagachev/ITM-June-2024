import matplotlib

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (10, 5)

fixed_df = pd.read_csv('bikes.csv')

fixed_df[:3]



