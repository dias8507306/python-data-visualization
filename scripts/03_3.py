import matplotlib.pyplot as plt

x = [1, 4, 8, 12, 16, 20]
y1 = [2, 10, 4, 8, 6, 14]   
y2 = [5, 2, 9, 3, 11, 7]   
y3 = [12, 8, 11, 5, 2, 4]  


locs = ['best', 'upper right', 'upper left', 'lower left',
        'lower right', 'right', 'center left', 'center right',
        'lower center', 'upper center', 'center']

plt.figure(figsize=(15, 12))

for i in range(3):
    for j in range(4):
        index = i * 4 + j
        if index < 11:
            plt.subplot(3, 4, index + 1)
            plt.title(locs[index])
            
            plt.plot(x, y1, color='blue', marker='*', linestyle='-', label='Line 1')
            plt.plot(x, y2, color='orange', marker='s', linestyle='--', label='Line 2')
            plt.plot(x, y3, color='purple', marker='^', linestyle='-.', label='Line 3')
            
        
            plt.legend(loc=locs[index], fontsize='small')
            
            plt.grid(True, alpha=0.3)
        else:
            break

plt.tight_layout()
plt.show()