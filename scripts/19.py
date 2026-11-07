import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Мәліметтер
np.random.seed(123)
vals = np.random.randint(11, size=(7, 7))

# Фигураны құру (figsize маңызды, оң жақтан орын қалдырады)
fig, ax = plt.subplots(figsize=(8, 5))

# График
gr = ax.pcolor(vals)

# Шкаланы орналастыру (bbox_to_anchor бірінші санын 1.05-тен 1.1-ге өзгерттік)
axins = inset_axes(ax, 
                   width="7%", 
                   height="50%", 
                   loc='lower left',
                   bbox_to_anchor=(1.1, 0.1, 1, 1), 
                   bbox_transform=ax.transAxes,
                   borderpad=0)

# Шкаланы баптау
cb = plt.colorbar(gr, cax=axins, ticks=[0, 2, 4, 6, 8, 10])

# Графиктің шеттері кесіліп қалмауы үшін
plt.subplots_adjust(right=0.85) 

plt.show()