import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

# Мәліметтерді дайындау
bc = mcolors.BASE_COLORS
np.random.seed(123)

groups = [f'P{i}' for i in range(7)]
counts = np.random.randint(0, len(bc), len(groups))
width = counts * 0.1

# ҚАТЕНІ ТҮЗЕТУ: np.random.randint(0, 3, 1)[0] деп жазу керек 
# немесе соңындағы 1-ді алып тастау керек.
colors = [['r', 'b', 'g'][int(np.random.randint(0, 3, 1)[0])] for _ in counts]

# Графикті салу
plt.bar(groups, counts, width=width, alpha=0.6, bottom=2, color=colors, edgecolor='k', linewidth=2)

plt.show()