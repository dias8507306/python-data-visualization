import numpy as np
import matplotlib.pyplot as plt

# 1. Мәліметтерді дайындау
np.random.seed(123)
vals = np.random.randint(10, size=(7, 7))

# 2. Графикті салу (Viridis палитрасы, 11 деңгей)
img = plt.pcolor(vals, cmap=plt.get_cmap('viridis', 11))

# 3. Горизонтальды Colorbar баптаулары
plt.colorbar(img, 
             orientation='horizontal', # Шкаланы астына қою
             shrink=0.9,               # Шкаланы 10%-ға қысқарту
             extend='max',             # Оң жағына "көрсеткі" (максимум) қосу
             extendfrac=0.2,           # Көрсеткінің өлшемі (шкаланың 20%-ы)
             extendrect=False,         # Көрсеткіні үшбұрыш қылу (True болса тіктөртбұрыш)
             drawedges=False)          # Деңгейлер арасындағы сызықтарды өшіру

plt.show()