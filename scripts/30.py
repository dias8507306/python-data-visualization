import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
offset = 0.4
data = np.array([[5, 10, 7], [8, 15, 5], [11, 9, 7]])

cmap = plt.get_cmap('tab20b')
b_colors = cmap(np.array([0, 8, 12]))
sm_colors = cmap(np.array([1, 2, 3, 9, 10, 11, 13, 14, 15]))

ax.pie(data.sum(axis=1), radius=1, colors=b_colors,
       wedgeprops=dict(width=offset, edgecolor='w'))

ax.pie(data.flatten(), radius=1-offset, colors=sm_colors,
       wedgeprops=dict(width=offset, edgecolor='w'))

plt.show()