import matplotlib.pyplot as plt

# Генерируем данные для параболы: y = x^2
x = list(range(-5, 6))
y = [i**2 for i in x]

plt.figure(figsize=(8, 5))
plt.plot(x, y)

# Добавляем аннотацию
plt.annotate(
    'min', 
    xy=(0, 0),         # Точка, на которую указывает стрелка (минимум)
    xycoords='data',   # Используем систему координат данных графика
    xytext=(0, 10),    # Положение самого текста 'min'
    textcoords='data', # Система координат для текста
    arrowprops=dict(
        facecolor='g', # Зеленый цвет заливки стрелки
        shrink=0.05    # Небольшой отступ стрелки от точек, чтобы не перекрывать их
    )
)

plt.show()