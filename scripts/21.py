import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# 1. Мәліметтер
np.random.seed(123)
vals = np.random.randint(11, size=(7, 7))

# 2. Фигура (оң жақтан орын қалдыру үшін figsize маңызды)
fig, ax = plt.subplots(figsize=(8, 5))

# 3. График
gr = ax.pcolor(vals)

# 4. Шкалаға арналған орын (bbox_to_anchor бірінші санын 1.1-ге қойдық)
axins = inset_axes(ax, 
                   width="7%", 
                   height="50%", 
                   loc='lower left',
                   bbox_to_anchor=(1.1, 0.25, 1, 1), 
                   bbox_transform=ax.transAxes,
                   borderpad=0)

# 5. Шкаланы баптау және мәтіндік белгілерді (labels) қосу
cbar = plt.colorbar(gr, cax=axins, ticks=[0, 5, 10], label='Value')
cbar.ax.set_yticklabels(['Low', 'Medium', 'High'])

# Графиктің оң жағындағы мәтіндер сыйып кетуі үшін шетін реттеу
plt.subplots_adjust(right=0.8)

plt.show()