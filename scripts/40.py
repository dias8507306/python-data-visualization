import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('iris')
y = df['petal_length']

sns.kdeplot(y, shade=True, kernel='cos')

sns.kdeplot(y, shade=True, kernel='gau')

plt.show()