import matplotlib.pyplot as plt

# Данные
x = [i for i in range(10)]
y = [i*2 for i in range(10)]

# Создание графика
plt.figure(figsize=(8, 5))
plt.plot(x, y)

# Подписи осей
plt.xlabel('Ось X')
plt.ylabel('Ось Y')


plt.show()