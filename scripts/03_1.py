import matplotlib.pyplot as plt

x = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
y2 = [4, 3, 1, 8, 12]
y3 = [6, 5, 8, 2, 9]  

plt.figure(figsize=(10, 6))


plt.plot(x, y1, color='blue', marker='o', linestyle='-', label='Көк сызық')
plt.plot(x, y2, color='orange', linestyle='--', linewidth=2, label='Dashed сызық')
plt.plot(x, y3, color='purple', marker='*', linestyle='-.', label='Жаңа сызық')

plt.legend(loc='lower right', fontsize='large', shadow=True)


plt.title("Өзгертілген стильдегі график")
plt.xlabel("X осі")
plt.ylabel("Y осі")
plt.grid(True, linestyle=':', alpha=0.6) 

plt.show()