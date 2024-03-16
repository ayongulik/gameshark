import pandas as pd

df = pd.read_csv('data/covid-2020-2022.csv', delimiter = ',')

# mendapatkan sample dari data
print(df.head())

# mendapatkan semua columns pada data
print(df.columns)

# mengakses nilai dari satu colum
print(df['countryterritoryCode'])

# mengakses nilai dari satu row
print(df.loc[0])

# mendapatkan possible values dari column tertentu
print(set(df['countryterritoryCode']))

# filtering data untuk negara2 benelux
df_benelux = df[df['countryterritoryCode'].isin(['BEL', 'NLD', 'LUX'])]

# filtering data untuk negara belgia dan tahun 2020
df_be2020 = df[(df['countryterritoryCode'] == 'BEL') & (df['year'] == 2020)]

# seleksi data
print(df_be2020[['cases', 'month', 'year']])

# max, min, mean, std, median
print(df_be2020['cases'].max())
print(df_be2020['cases'].min())
print(df_be2020['cases'].mean())
print(df_be2020['cases'].median())
print(df_be2020['cases'].std())

# mendapatkan beberapa statistik sekaligus berdasarkan kode negara
stat_covid_describe = df[['cases', 'deaths', 'countryterritoryCode']].groupby(['countryterritoryCode']).describe()
print(stat_covid_describe.loc['ITA'])

def q95(x):
    return x.quantile(0.95)

# mendapatkan beberapa statistik sekaligus dengan mendefinisikan fungsi statistik yang ingin dipakai
stat_covid_agg = df['cases'].agg(['mean', 'median', q95])

# sorting data
print(df_be2020[['month', 'cases']].sort_values(by = 'cases', ascending = False))
