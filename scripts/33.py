import sys
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Консольде қазақша әріптер дұрыс шығуы үшін (UTF-8 орнату)
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

# Стильді баптау
sns.set_style("darkgrid")

# --- 1. ГИСТОГРАММА (PENGUINS) ---
print("Penguins деректер жиынтығы жүктелуде...")
penguins = sns.load_dataset("penguins")

plt.figure(figsize=(10, 6))
# Пингвиндердің қанат ұзындығының таралуы
sns.histplot(data=penguins, x="flipper_length_mm", hue="species", kde=True, palette="magma")
plt.title("Penguins: Қанат ұзындығының таралуы")
plt.show()


# --- 2. VIOLIN PLOT (TIPS) ---
print("Tips деректер жиынтығы жүктелуде...")
tips = sns.load_dataset("tips")

plt.figure(figsize=(10, 6))
# Шот сомасының апта күндеріне байланысты скрипка графигі
sns.violinplot(data=tips, x="day", y="total_bill", hue="smoker", split=True, palette="Pastel1")
plt.title("Tips: Шот сомасы және темекі шегушілер")
plt.show()


# --- 3. JOINT PLOT (Жаңа график түрі - екі айнымалының байланысы) ---
print("Joint plot құрылуда...")
# Бұл график бір уақытта нүктелік графикті де, гистограмманы да көрсетеді
g = sns.jointplot(data=penguins, x="bill_length_mm", y="bill_depth_mm", hue="species", palette="viridis")
g.fig.suptitle("Тұмсық ұзындығы мен енінің байланысы", y=1.02)
plt.show()

print("Барлық графиктер сәтті шықты!")