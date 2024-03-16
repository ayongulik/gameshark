import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

df = pd.read_csv('data/covid-2020-2022.csv', delimiter = ',')

# Step 1: filtering data
df_filtered = df[df['countriesAndTerritories'].isin(['Luxembourg', 'Belgium', 'Netherlands'])]

# Step 2: grouping 'month' dan aggregate
cases_bymonth = df_filtered.groupby(['month']).agg(cases = ('cases', 'sum'))

# Step 3: inisialisasi plot
fig, ax = plt.subplots()

df_filtered.plot(cases_bymonth.index, cases_bymonth['cases'])

# Step 4: penambahan label x dan y axis
ax.set_xlabel('Month')
ax.set_xlabel('Cases')

# Step 5: penambahan judul plot
ax.set_title('Trend of COVID-19 cases in Belgium (2020)')

ax.xaxis.set_major_locator(ticker.FixedLocator(cases_bymonth.index))