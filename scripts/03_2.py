import matplotlib.pyplot as plt


x = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
y2 = [4, 3, 1, 8, 12]


locs = ['best', 'upper right', 'upper left', 'lower left',
        'lower right', 'right', 'center left', 'center right',
        'lower center', 'upper center', 'center']


plt.figure(figsize=(12, 10))


for i in range(3): 
    for j in range(4): 
        index = i * 4 + j
        if index < 11:
            plt.subplot(3, 4, index + 1) 
            plt.title(locs[index]) 
            
            plt.plot(x, y1, 'o-r', label='line 1') 
            plt.plot(x, y2, 'o-.g', label='line 2') 
            
            plt.legend(loc=locs[index])
        else:
            break


plt.tight_layout()
plt.show() 