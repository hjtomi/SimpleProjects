import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
from natsort import natsorted
import datetime

FIRST_DATE = datetime.date(2021, 1, 1)
NUMBER_OF_DAYS = 815
EUR_TO_HUF = 380
DATE_FORMAT = '%Y-%m-%d'


def rename_files():
    """
    Renames files that have its month written out with letters
    to ones that have numbers as months.
    :return: None
    """

    months = [None, "Január", "Február", "Március", "Április", "Május", "Június", "Július", "Augusztus", "Szeptember",
              "Október", "November", "December"]

    file_names: list[str]
    file_names = os.listdir('Excelek')
    stripped_file_names: list[str]
    stripped_file_names = list(map(lambda x: x.removesuffix('.xlsx'), file_names))

    for file_name, stripped_file_name in zip(file_names, stripped_file_names):
        if stripped_file_name[-1] not in range(10):
            honap = stripped_file_name.partition(".")[2]
            szam = months.index(honap)
            os.rename(f'Excelek/{file_name}', f'{file_name.partition(".")[0]}.{szam}.xlsx')


def create_grand_excel():
    file_names = natsorted(os.listdir('Excelek'))
    dfs = []

    for file_name in file_names:
        df = pd.read_excel(f'Excelek/{file_name}', header=4, skipfooter=6)
        df.rename(columns={'Unnamed: 0': 'nap', 'Kártyás fizetés': 'kartyas_fizetes'}, inplace=True)
        dfs.append(df)

    for df in dfs[1:]:
        dfs[0] = dfs[0].merge(df, how='outer')

    grand_df = dfs[0]
    grand_df.to_excel('grand-penztargep.xlsx', sheet_name='Munka1')


def dates_to_grand():
    def dates_generator():
        for i in range(NUMBER_OF_DAYS + 1):
            yield FIRST_DATE + datetime.timedelta(i)

    df = pd.read_excel('grand-penztargep.xlsx')
    df['datum'] = pd.Series(list(dates_generator()))
    df.rename(columns={'Összesen': 'osszesen'}, inplace=True)
    df.replace('ZÁRVA', 0, inplace=True)
    df.fillna(0, inplace=True)
    df.drop(labels='nap', axis='columns', inplace=True)
    cols = df.columns.tolist()
    order = [8, 0, 1, 2, 3, 6, 4, 5, 7]
    cols = [cols[i] for i in order]
    df = df[cols]
    df.to_excel('grand-penztargep-datummal.xlsx', index=False)


def fill_eur_huf_dates():
    df_huf = pd.read_excel('EUR_HUF Historical Data.xlsx')

    for i, row in enumerate(df_huf[:-1].iterrows()):
        current_row_contents = row[1]
        dt_date = row[1][0]
        dt_next_date = df_huf.loc[i+1][0]
        day_diff = (dt_next_date - dt_date).days

        if day_diff > 1:
            for j in range(day_diff-1):
                current_row_contents[0] = pd.to_datetime(current_row_contents[0]) + datetime.timedelta(1)
                current_row_contents[6] = '0.00%'
                df_huf.loc[len(df_huf.index)] = current_row_contents

    df_huf['Date'] = pd.to_datetime(df_huf['Date'])
    df_huf = df_huf.sort_values(by='Date')
    df_huf.to_excel('EUR_HUF Historical Data Date-Filled.xlsx')


def make_income_relative():
    df_pg = pd.read_excel('grand-penztargep-datummal.xlsx')
    df_huf = pd.read_excel('EUR_HUF Historical Data Date-Filled.xlsx')

    df_pg['relativ_osszesen'] = df_pg['osszesen'] * round(377 / df_huf['Price'], 2)
    df_pg['relativ_0.05'] = df_pg[0.05] * round(377 / df_huf['Price'], 2)
    df_pg['relativ_0.18'] = df_pg[0.18] * round(377 / df_huf['Price'], 2)
    df_pg['relativ_0.27'] = df_pg[0.27] * round(377 / df_huf['Price'], 2)
    df_pg['relativ_kartyas_fizetes'] = df_pg['kartyas_fizetes'] * round(377 / df_huf['Price'], 2)
    df_pg['relativ_Storno 5%'] = df_pg['Storno 5%'] * round(377 / df_huf['Price'], 2)
    df_pg['relativ_Storno 18%'] = df_pg['Storno 18%'] * round(377 / df_huf['Price'], 2)
    df_pg['relativ_Storno 27%'] = df_pg['Storno 27%'] * round(377 / df_huf['Price'], 2)
    df_pg['datum'] = df_pg['datum'].dt.date

    df_pg.to_excel('grand-penztargep-datummal-relativokkal.xlsx', index=False)
