import pandas as pd
import plotly.express as px

df_havi = pd.read_excel('osszesitett-cuki-masolat.xlsx')
df_napi = pd.read_excel('grand-penztargep-datummal.xlsx')

# tobb reszbol allo bar chart
# fig = px.bar(df_havi, x='datum', y=['penztargep', 'borravalo', 'fekete'])
# fig.show()

# line plot
# fig = px.line(df_havi, x='datum', y=['osszes', 'penztargep', 'fekete', 'borravalo'], markers=True)
# fig.show()

# box plot
# df_napi['datum']: pd.DatetimeIndex
# fig = px.box(x=df_napi['datum'].apply(lambda x: x.strftime('%Y-%m')), y=df_napi['osszesen'], points='all')
# fig.show()
