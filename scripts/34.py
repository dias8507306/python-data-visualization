import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Қазақша әріптер үшін UTF-8 реттеу
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

# Мәліметтерді жүктеу
iris = sns.load_dataset("iris")
mpg = sns.load_dataset("mpg")

# --- ЭКСПЕРИМЕНТ 1: Iris-ке тән "Pairplot"-ты MPG-ге қолдану ---
# Iris-те біз гүл түрлерін (species) ажыратсақ, 
# MPG-де көліктің шыққан жерін (origin: USA, Japan, Europe) ажыратып көреміз.
print("Эксперимент 1: MPG деректеріне Pairplot салу...")
sns.pairplot(mpg[['mpg', 'horsepower', 'weight', 'origin']], hue="origin", palette="viridis")
plt.suptitle("MPG-дегі көліктердің шыққан жері бойынша кластерлері", y=1.02)
plt.show()


# --- ЭКСПЕРИМЕНТ 2: Iris-тің Swarmplot-ын MPG-ге салу ---
# Iris-тегі сияқты 'species' орнына көліктің цилиндр санын (cylinders) қоямыз.
print("Эксперимент 2: MPG-дегі Swarmplot...")
plt.figure(figsize=(10, 6))
# Цилиндр санына байланысты ат күші (horsepower) қалай таралатынын көреміз
sns.swarmplot(x="cylinders", y="horsepower", data=mpg, hue="origin", size=4)
plt.title("Цилиндр саны мен ат күшінің байланысы (Swarmplot стилі)")
plt.show()


# --- ЭКСПЕРИМЕНТ 3: Мүлдем басқа стиль (JointPlot) ---
print("Эксперимент 3: MPG-дегі тығыздық графигі...")
# Көліктің салмағы мен оның үнемділігі (mpg) арасындағы байланыс
g = sns.jointplot(data=mpg, x="weight", y="mpg", hue="origin", kind="kde", fill=True, alpha=0.5)
g.fig.suptitle("Көлік салмағы мен үнемділігінің тығыздығы", y=1.03)
plt.show()

print("Эксперимент аяқталды!")