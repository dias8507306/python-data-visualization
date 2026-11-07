import matplotlib.pyplot as plt

plt.close('all')

# Мәліметтер
x = [1, 4, 8, 12, 16, 20]
y1 = [2, 10, 4, 8, 6, 14]   
y2 = [5, 2, 9, 3, 11, 7]   
y3 = [12, 8, 11, 5, 2, 4]   

# Аңыздың орналасу орындары (11 стандартты мән)
locs = ['best', 'upper right', 'upper left', 'lower left',
        'lower right', 'right', 'center left', 'center right',
        'lower center', 'upper center', 'center']

# 15 график жасау үшін 5 қатар және 3 баған қолданамыз
plt.figure(figsize=(15, 25))

for i in range(5):           # 5 қатар
    for j in range(3):       # 3 баған
        index = i * 3 + j    # Индекс 0-ден 14-ке дейін
        
        plt.subplot(5, 3, index + 1) 
        
        # 11 орынды 15 графикке бөлу үшін қалдық арқылы есептейміз
        current_loc = locs[index % len(locs)]
        plt.title(f"Plot {index + 1}: loc='{current_loc}'")
        
        plt.plot(x, y1, color='blue', marker='*', linestyle='-', label='Line 1')
        plt.plot(x, y2, color='orange', marker='s', linestyle='--', label='Line 2')
        plt.plot(x, y3, color='purple', marker='^', linestyle='-.', label='Line 3')
        
        # Аңыз баптаулары
        plt.legend(
            loc=current_loc, 
            fontsize=7,
            edgecolor='r', 
            labelspacing=2,
            handlelength=2,
            borderpad=0.2,
            facecolor='y',
            handletextpad=0.2
        )

        plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('15_plots.png')
plt.show()