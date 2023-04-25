import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly as py

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

df: pd.DataFrame
df = pd.read_excel('grand-penztargep-datummal.xlsx').iloc[577:].reset_index().drop(columns='index')
print(df)

df['hetnap'] = df['datum'].dt.day_name()
print(df)

print(df[df['hetnap'] == 'Monday'][0.05].mean())

df_weekday = df.groupby('hetnap').mean()
print(df_weekday)

df_weekday = df_weekday.reset_index()
print(df_weekday)

df_weekday['hetnap'] = pd.Categorical(df_weekday['hetnap'], categories=weekdays, ordered=True)
print(df_weekday)

df_weekday = df_weekday.sort_values('hetnap')
print(df_weekday)

sns.barplot(x='hetnap', y='osszesen', data=df_weekday)
plt.title('Átlagbevétel a hét napjain (2022.08.01 - 2023.03.31)', fontsize=40)
plt.xlabel('Het Napjai', fontsize=30)
plt.xticks(fontsize=15)
plt.ylabel('Atlag Penztargepes Bevetel', fontsize=30)
plt.yticks(ticks=range(0, 625001, 25000), fontsize=15)

plt.grid()
plt.show()
