import numpy as np
import matplotlib.pyplot as plt

# Мәліметтерді дайындау
x = np.arange(0.0, 5, 0.01)
y = np.cos(x * np.pi)

# Графикті сызу
plt.plot(x, y, c='r') # Қызыл сызық

# График пен Х осінің арасын бояу
plt.fill_between(x, y, color='blue', alpha=0.3)

# Экранға шығару
plt.show()