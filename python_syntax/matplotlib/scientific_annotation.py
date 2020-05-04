import matplotlib.pyplot as plt
import seaborn as sns
from statannot import add_stat_annotation

sns.set(style="whitegrid")
df = sns.load_dataset("tips")

print(df)


x = "day"
y = "total_bill"
order = ['Sun', 'Thur', 'Fri', 'Sat']

fig,ax = plt.subplots(ncols=2)
sns.boxplot(ax=ax[0], data=df, x=x, y=y, order=order)
add_stat_annotation(ax[0], data=df, x=x, y=y, order=order,
                    box_pairs=[("Thur", "Fri"), ("Thur", "Sat"), ("Fri", "Sun")],
                    test='Mann-Whitney', text_format='star', loc='outside', verbose=2)

x = "day"
y = "total_bill"
hue = "smoker"
sns.boxplot(ax=ax[1], data=df, x=x, y=y, hue=hue)
add_stat_annotation(ax[1], data=df, x=x, y=y, hue=hue,
                    box_pairs=[(("Thur", "No"), ("Fri", "No")),
                                 (("Sat", "Yes"), ("Sat", "No")),
                                 (("Sun", "No"), ("Thur", "Yes"))
                                ],
                    test='t-test_ind', text_format='full', loc='inside', verbose=2)
plt.legend(loc='upper left', bbox_to_anchor=(1.03, 1))
plt.show()