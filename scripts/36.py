import seaborn as sns
import matplotlib.pyplot as plt

# Установка стиля (опционально, для красоты)
sns.set_theme()

# Загрузка демонстрационного набора данных
iris = sns.load_dataset("iris")

# --- 1. Контекст "paper" (самый мелкий, для научных статей) ---
sns.set_context("paper")
plt.figure(figsize=(8, 5))
sns.scatterplot(x='sepal_length', y='petal_length', data=iris)
plt.title("Контекст: paper")
plt.show()

# --- 2. Контекст "notebook" (по умолчанию) ---
sns.set_context("notebook")
plt.figure(figsize=(8, 5))
sns.scatterplot(x='sepal_length', y='petal_length', data=iris)
plt.title("Контекст: notebook")
plt.show()

# --- 3. Контекст "talk" (крупнее, для презентаций) ---
sns.set_context("talk")
plt.figure(figsize=(8, 5))
sns.scatterplot(x='sepal_length', y='petal_length', data=iris)
plt.title("Контекст: talk")
plt.show()

# --- 4. Контекст "poster" (самый крупный, для плакатов) ---
sns.set_context("poster")
plt.figure(figsize=(8, 5))
sns.scatterplot(x='sepal_length', y='petal_length', data=iris)
plt.title("Контекст: poster")
plt.show()

# --- 5. Вывод параметров текущего контекста в консоль ---
print("Параметры контекста notebook:")
print(sns.plotting_context("notebook"))

# --- 6. Контекст с ручной модификацией параметров (RC) ---
sns.set_context("notebook", font_scale=1.5, rc={
    'lines.markersize': 15,
    'xtick.labelsize': 15.0, 
    'ytick.labelsize': 15.0
})
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sepal_length', y='petal_length', data=iris)
plt.title("Контекст: notebook (модифицированный)")
plt.show()