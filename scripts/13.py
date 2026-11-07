import matplotlib.pyplot as plt

# Данные
x = range(0, 10)
y = range(0, 10)

plt.figure(figsize=(8, 5))
plt.plot(x, y)

# Настройка заголовка (как на последнем скриншоте)
plt.title('Title', 
          alpha=0.5,        # Прозрачность 50%
          color='r',        # Красный цвет
          fontsize=18,      # Размер шрифта
          fontstyle='italic', # Курсив
          fontweight='bold',  # Жирный
          linespacing=10)   # Интервал (если бы было несколько строк)

plt.show()