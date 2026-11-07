import matplotlib.pyplot as plt

# Данные для графика
plt.plot(range(0, 10), range(0, 10))

# Настройка свойств текстового бокса
# boxstyle='darrow' создает двустороннюю стрелку
bbox_properties = dict(
    boxstyle='darrow, pad=0.3', 
    ec='k',   # цвет границы (edgecolor) - черный
    fc='y',   # цвет заливки (facecolor) - желтый
    ls='-',   # стиль линии (linestyle) - солидная
    lw=3      # толщина линии (linewidth)
)

# Добавление текста с боксом
# Координаты (2, 7) соответствуют положению на осях
plt.text(2, 7, 'MARIAMAGDALENA', fontsize=15, bbox=bbox_properties)

plt.show()