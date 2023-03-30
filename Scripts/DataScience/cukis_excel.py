import pandas as pd
from matplotlib import pyplot as plt
import random
import numpy as np

df = pd.read_excel('Beérkező áruk-2022.szeptember.xls')
# Csak azokat tartjuk meg amelyeknek osszesen tobb mint 0 volt
df = df[df['osszesen'] > 0]
print(df.columns)


def suti_osszehasonlitas():
    def random_color():
        r = lambda: random.randint(0, 255)
        return '#%02X%02X%02X' % (r(), r(), r())

    nevek = []
    for nev, osszesen in zip(df['nev'], df['osszesen']):
        i = 10
        while nev[:i] in nevek:
            i += 1

        plt.bar(nev[:i], osszesen, color=random_color(), width=0.8)
        nevek.append(nev[:i])

    plt.ylim([0, 600])
    plt.ylabel("Osszesen")
    plt.xticks(rotation=45, fontsize=5)

    plt.grid()
    plt.tight_layout()
    plt.show()


def eladasok_a_honap_folyaman():
    labels = ['1-4', '5-10', '11-17', '18-25', '26-30']
    colors = ['#48dde0', '#48abe0', '#4878e0', '#4848e0', '#5748e0']
    plt.pie(x=[df['1-4'].sum(), df['5-10'].sum(), df['11-17'].sum(), df['18-25'].sum(), df['26-30'].sum()],
            labels=labels,
            colors=colors,
            wedgeprops={'edgecolor': 'black'},
            )
    plt.show()


def osszesen_vs_ertek():
    # N = len(df['osszesen'])
    #
    # ind = np.arange(N)  # the x locations for the groups
    # width = 0.35  # the width of the bars
    #
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # rects1 = ax.bar(ind, df['osszesen'], width, color='royalblue')
    #
    # rects2 = ax.bar(ind + width, df['ertek'], width, color='seagreen')
    #
    # # add some
    # ax.set_ylabel('Scores')
    # ax.set_title('Scores by group and gender')
    # ax.set_xticks(ind + width / 2)
    #
    # ax.legend((rects1[0], rects2[0]), ('Men', 'Women'))
    #
    # plt.show()

    N = len(df['osszesen'])
    ind = np.arange(N)
    width = 0.3

    plt.xticks(rotation=45, fontsize=7)

    ax1 = plt.gca()
    ax2 = ax1.twinx()

    ax1.bar(df['nev'].str[:7], df['osszesen'], width, color='#B8621B', label='osszesen')
    ax2.bar(ind + width, df['ertek'], width, color='#262A56', label='ertek')

    ax1.legend()
    ax2.legend()

    plt.tight_layout()
    plt.show()


suti_osszehasonlitas()
