import seaborn as sns
import matplotlib.pyplot as plt

# 1. Деректерді жүктеу
data = sns.load_dataset('flights')

# 2. Rugplot салу (тек X осінің бойымен)
sns.rugplot(data["passengers"])

# 3. Көрсету
plt.show()