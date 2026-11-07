import matplotlib.pyplot as plt


x = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
y2 = [4, 3, 1, 8, 12]

plt.figure(figsize=(12, 5))


plt.subplot(1, 2, 1) 
plt.plot(x, y1, 'o-r', label='line 1') 
plt.plot(x, y2, 'o-.g', label='line 1')
plt.legend() 
plt.title("Рисунок 3.1 (label арқылы)")


plt.subplot(1, 2, 2) 
plt.plot(x, y1, 'o-r')
plt.plot(x, y2, 'o-.g')
plt.legend(['L1', 'L2']) 
plt.title("Рисунок 3.2 (тізім арқылы)")


plt.tight_layout()
plt.show()