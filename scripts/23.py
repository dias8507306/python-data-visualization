import matplotlib.pyplot as plt

x = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
y2 = [4, 3, 1, 8, 12]

plt.figure(figsize=(12, 7))

# Бірінші сызық: қызыл түс, дөңгелек нүктелер, қалыңдығы 5
plt.plot(x, y1, 'o-r', alpha=0.7, label='first', lw=5, mec='b', mew=2, ms=10)

# Екінші сызық: жасыл түс, үшбұрыш нүктелер, пунктир сызық
plt.plot(x, y2, 'v-.g', label='second', mec='r', lw=2, mew=2, ms=12)

plt.legend() # Шартты белгілерді шығару
plt.grid(True) # Тор көздерін қосу
plt.show()