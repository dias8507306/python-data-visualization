import matplotlib.pyplot as plt

x = [i for i in range(10)]
y = [i*2 for i in range(10)]

plt.figure(figsize=(8, 6))
plt.plot(x, y)

# Подписи осей с переносом строки (\n)
plt.xlabel('Ось X\nНезависимая величина', fontsize=14, fontweight='bold', labelpad=10)
plt.ylabel('Ось Y\nЗависимая величина', fontsize=14, fontweight='bold', labelpad=10)

plt.show()