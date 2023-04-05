import matplotlib.axes
import pandas as pd
import matplotlib.pyplot as plt

jegyek_df = pd.read_excel('TantargyJegyek.xlsx')
print(jegyek_df)
print(plt.style.available)
plt.style.use('ggplot')

ax: matplotlib.axes.Axes
fig, ax = plt.subplots()

# ax.bar(range(6), range(6))
# ax.set(xlim=(0, 10), xticks=range(11))

ax.scatter()

plt.show()
