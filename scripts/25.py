import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

vals = np.random.randint(11, size=(7, 7))
fig, ax = plt.subplots()
gr = ax.pcolor(vals)

axins = inset_axes(ax, 
                   width="5%",     
                   height="50%",     
                   loc='center right',  
                   bbox_to_anchor=(1.05, 0.25, 1, 1), 
                   bbox_transform=ax.transAxes)

plt.colorbar(gr, cax=axins)
plt.show()