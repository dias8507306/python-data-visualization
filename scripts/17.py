import numpy as np
import matplotlib.pyplot as plt

# Кездейсоқ сандар генераторының ретін бекіту
np.random.seed(123)

# 7x7 өлшемді матрица құрастыру (0-ден 9-ға дейінгі сандар)
vals = np.random.randint(10, size=(7, 7))

# Түсті картаны (pcolor) құру
plt.pcolor(vals)

# Түстердің нені білдіретінін көрсететін шкала қосу (міндетті емес, бірақ пайдалы)
plt.colorbar()

# Графикті экранға шығару
plt.show()

