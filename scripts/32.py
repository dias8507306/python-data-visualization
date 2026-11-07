import seaborn as sns
import matplotlib.pyplot as plt

# 1. Загрузка данных
flights = sns.load_dataset("flights")

# Создаем общее полотно для сравнения всех стилей
styles = ['darkgrid', 'whitegrid', 'dark', 'white', 'ticks']
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

# 2. Отрисовка стандартных стилей в цикле
for i, style in enumerate(styles):
    sns.set_style(style)
    sns.lineplot(x='year', y='passengers', data=flights, ax=axes[i])
    axes[i].set_title(f'Style: {style}')

# 3. Демонстрация модифицированного стиля (Рисунок 7.6)
# Мы меняем цвет меток осей (зеленый), границ (красный) и подписей (синий)
custom_params = {
    'axes.labelcolor': 'blue', 
    'axes.edgecolor': 'red', 
    'xtick.color': 'green'
}
sns.set_style("whitegrid", rc=custom_params)
sns.lineplot(x='year', y='passengers', data=flights, ax=axes[5])
axes[5].set_title('Custom Whitegrid (Modded)')

# Автоматическое выравнивание
plt.tight_layout()

# Вывод параметров стиля в консоль (как в учебнике)
print("Текущие параметры стиля:")
print(sns.axes_style())

# Показать графики
plt.show()