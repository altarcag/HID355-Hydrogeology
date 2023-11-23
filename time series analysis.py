import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("./hydro.csv")

data = data.drop(columns='Unnamed: 0')
print(data.head())

# Set the 'year' column as the index
data.set_index('year', inplace=True)

# Calculate the arithmetic mean
mean_value = data['precipitation (mm)'].mean()

# Print the result
def mean():
    pr_mean = data['precipitation (mm)'].mean()
    mean_rounded = round(pr_mean, 2)
    return mean_rounded

mean_res = mean()
print("arithmetic mean: ", mean_res)

# deviation of precipitation
pd.set_option('display.float_format', '{:.2f}'.format)
pr_dev = data['precipitation (mm)'] - mean_value
print(pr_dev)
#cumulative deviation
cum_dev = np.cumsum(pr_dev)

print(cum_dev)

data['precipitation (mm)'].plot.bar(width=0.9)

plt.axhline(mean_res, color='red', linestyle='--', label='Mean')
plt.xlabel("Years", fontsize=15)
plt.ylabel("P (mm)", fontsize=15)
plt.show()
