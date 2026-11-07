import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('penguins')

sns.kdeplot(data=df, x='bill_length_mm', y='bill_depth_mm', shade=True ,cmap='rainbow', cbar=True)

plt.show()