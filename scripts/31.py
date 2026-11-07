import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Настройка стиля (чтобы графики выглядели современно)
sns.set_theme()

# --- 1. ТОЧЕЧНЫЙ ГРАФИК (Набор данных MPG) ---
print("Загрузка данных MPG...")
mpg = sns.load_dataset("mpg")
print(mpg.head())

# Построение зависимости ускорения от л.с.
sns.relplot(x="horsepower", y="acceleration", size="cylinders", data=mpg)
plt.title("Зависимость ускорения от лошадиных сил")
plt.show() # В VS Code откроется отдельное окно с графиком


# --- 2. ЛИНЕЙНЫЙ ГРАФИК (Набор данных FLIGHTS) ---
print("\nЗагрузка данных FLIGHTS...")
flights = sns.load_dataset("flights")
print(flights.head())

# Построение графика пассажиров по годам
sns.relplot(x="year", y="passengers", kind="line", legend="full", data=flights)
plt.title("Количество пассажиров по годам")
plt.show()


# --- 3. КАТЕГОРИАЛЬНЫЕ ДАННЫЕ (Набор данных IRIS) ---
print("\nЗагрузка данных IRIS...")
iris = sns.load_dataset("iris")
print(iris.head())

# Вариант 1: Точечная диаграмма (Swarmplot)
sns.catplot(x="species", y="sepal_length", kind="swarm", data=iris)
plt.title("Распределение длины чашелистика (Swarmplot)")
plt.show()

# Вариант 2: Ящик с усами (Boxplot)
plt.figure(figsize=(8, 6)) # Создаем новую фигуру для boxplot
sns.boxplot(x="species", y="sepal_length", data=iris)
plt.title("Распределение длины чашелистика (Boxplot)")
plt.show()

print("\nВсе графики построены!")