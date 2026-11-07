import seaborn as sns
import matplotlib.pyplot as plt

flights = sns.load_dataset("flights")

sns.set_style("darkgrid")
sns.lineplot(x='year', y='passengers', data=flights)
plt.title("Flights Data - Darkgrid Style")
plt.show()

