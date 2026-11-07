import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset('diamonds')

sns.rugplot(data["price"], height=0.3, color='r', axis='y')

plt.show()