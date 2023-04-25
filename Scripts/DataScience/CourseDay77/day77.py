import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.option_context('display.max_columns', 10)

# Cleaning strarting Dataframe
# df = pd.read_csv('cost_revenue_dirty.csv')
# df.dropna(inplace=True)
# df.drop_duplicates(inplace=True)
# df.rename(columns={
#     'Rank': 'rank',
#     'Release_Date': 'reldate',
#     'Movie_Title': 'title',
#     'USD_Production_Budget': 'prodbud',
#     'USD_Worldwide_Gross': 'worldg',
#     'USD_Domestic_Gross': 'domg'}, inplace=True)
# print(df.columns)
# df['reldate'] = pd.to_datetime(df['reldate'])
# df['prodbud'] = pd.to_numeric(df['prodbud'].str.replace('$', '').str.replace(',', ''))
# df['worldg'] = pd.to_numeric(df['worldg'].str.replace('$', '').str.replace(',', ''))
# df['domg'] = pd.to_numeric(df['domg'].str.replace('$', '').str.replace(',', ''))
# df.to_csv('cost_revenue_clean.csv', index=False)

df = pd.read_csv('cost_revenue_clean.csv')
df = df.query('worldg > 0 and prodbud > 0')
sns.relplot(df, x='reldate', y='prodbud', size='worldg')
plt.show()
