import matplotlib.pyplot as plt

# Данные для линейного графика
x = range(0, 10)
y = range(0, 10)

plt.figure(figsize=(8, 5))
plt.plot(x, y)

# Добавление текстового блока внутри графика
# 0, 7 — координаты по осям X и Y
plt.text(0, 7, 'MARIAMAGDALENA', fontsize=15)



plt.show()