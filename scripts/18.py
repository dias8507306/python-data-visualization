import numpy as np
import matplotlib.pyplot as plt

# Кездейсоқ сандардың бірдей шығуы үшін
np.random.seed(123)

# 7x7 өлшемді матрица (0 мен 9 аралығындағы сандар)
vals = np.random.randint(10, size=(7, 7))

# Графикті құру: 'viridis' түстер палитрасын 11 деңгейге бөлу
plt.pcolor(vals, cmap=plt.get_cmap('viridis', 11))

# Түс шкаласын қосу
plt.colorbar()

# Экранға шығару
plt.show()
