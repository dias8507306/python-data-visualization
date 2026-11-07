import matplotlib.pyplot as plt

# Данные для графика
plt.plot(range(0, 10), range(0, 10))

# Настройка вертикального заголовка внутри графика
plt.title('Title', 
          fontsize=17, 
          position=(0.7, 0.2), # Смещение вправо на 70% и вверх на 20%
          rotation='vertical') # Вертикальная ориентация

plt.show()