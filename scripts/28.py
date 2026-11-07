import matplotlib.pyplot as plt
import numpy as np

# 1. Мәліметтер мен рандомды баптау
np.random.seed(123)
rnd = np.random.randint

cat_par = [f'P{i}' for i in range(5)]
g1 = [10, 21, 34, 12, 27]

# Әр баған үшін төменгі және жоғарғы қателік мәндерін жасау
error = np.array([[rnd(2, 7), rnd(2, 7)] for _ in range(len(cat_par))]).T

# 2. Екі графикті (1 қатар, 2 баған) құру
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# Сол жақтағы график: Тұрақты қателік мәні (yerr=5)
axs[0].bar(cat_par, g1, yerr=5, ecolor='r', alpha=0.5, edgecolor='b', linewidth=2)

# Оң жақтағы график: Кездейсоқ қателік мәндері (yerr=error)
axs[1].bar(cat_par, g1, yerr=error, ecolor='r', alpha=0.5, edgecolor='b', linewidth=2)

# 3. Нәтижені көрсету
plt.tight_layout() # Графиктер бір-біріне мінгесіп қалмауы үшін
plt.show()