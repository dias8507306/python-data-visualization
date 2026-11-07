import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')
y = df['age'].dropna() 

sns.kdeplot(y, shade=True, label="default")
sns.kdeplot(y, shade=True, bw=10, label="bw=10")
sns.kdeplot(y, shade=True, bw=70, label="bw=70")

plt.legend()
plt.show()