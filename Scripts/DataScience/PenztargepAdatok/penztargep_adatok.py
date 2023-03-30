import pandas as pd
import matplotlib.pyplot as plt
import os
from natsort import natsorted
import datetime

FIRST_DATE = datetime.date(2021, 1, 1)
NUMBER_OF_DAYS = 815


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
    df.to_excel('grand-excel-datummal.xlsx')
