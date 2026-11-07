import matplotlib.pyplot as plt
import numpy as np

# 1. Мәліметтерді дайындау
cat_par = [f'P{i}' for i in range(5)]
g1 = [10, 21, 34, 12, 27]
g2 = [17, 15, 25, 21, 26]

width = 0.3  # Бағандардың ені
x = np.arange(len(cat_par))  # X осіндегі позициялар

# 2. Графикті құру
fig, ax = plt.subplots()

# Бағандарды бір-біріне тигізіп, екі жаққа жылжыту
rects1 = ax.bar(x - width/2, g1, width, label='g1')
rects2 = ax.bar(x + width/2, g2, width, label='g2')

# 3. Графикті безендіру
ax.set_title('Пример групповой диаграммы')
ax.set_xticks(x)
ax.set_xticklabels(cat_par)
ax.legend() # Аңызды (g1, g2) көрсету

# 4. Нәтижені шығару
plt.show()