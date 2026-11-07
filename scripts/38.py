import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('geyser')

sns.kdeplot(data=df, x='duration', y='waiting', shade=True, cmap='rainbow', cbar=True)

plt.show()