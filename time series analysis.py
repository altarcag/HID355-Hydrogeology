import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("./hydro.csv")
data = data.drop(columns='Unnamed: 0')
print(data.head())

# Set the 'year' column as the index
data.set_index('year', inplace=True)
#arithmetic mean
mean_value = data['precipitation (mm)'].mean()

def mean():
    pr_mean = data['precipitation (mm)'].mean()
    mean_rounded = round(pr_mean, 2)
    return mean_rounded

mean_res = mean()

# deviation of precipitation
pd.set_option('display.float_format', '{:.2f}'.format)
pr_dev = data['precipitation (mm)'] - mean_value
#cumulative deviation
cum_dev = np.cumsum(pr_dev)

#combining year, pr_dev, and cum_dev into a DataFrame
result_df = pd.DataFrame({'Precipitation': data['precipitation (mm)'], 'Deviation from mean': pr_dev.values, 'Cumulative Deviation': cum_dev})
#the DataFrame
print(result_df)
print("arithmetic mean: ", mean_res)

plt.figure(figsize=(12, 6))
data['precipitation (mm)'].plot.bar(width=0.9)
plt.axhline(mean_res, color='red', linestyle='--', label='Mean')
plt.xlabel("Years", fontsize=15, labelpad=5)
plt.ylabel("P (mm)", fontsize=15, labelpad=5)
plt.title("Precipitation Graph", fontsize=15, pad=10)
plt.show()

plt.figure(figsize=(12, 6))
cum_dev.plot()
plt.xticks(cum_dev.index, rotation=90)
plt.axhline(0, color='grey', linestyle='--')
plt.xlabel("Years", fontsize=15, labelpad=5)
plt.ylabel("P (mm)", fontsize=15, labelpad=5)
plt.title("Cumulative Deviation of Precipitation graph", fontsize=15, pad=10)
plt.show()
