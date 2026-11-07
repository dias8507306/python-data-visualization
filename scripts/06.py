import matplotlib.pyplot as plt

# Список начертаний шрифта
weight = ['light', 'normal', 'bold']

# Создаем фигуру
plt.figure(figsize=(12, 4))

for i, lc in enumerate(['left', 'center', 'right']):
    plt.subplot(1, 3, i+1)
    
    # Настройка заголовка согласно твоим параметрам
    plt.title(label=lc, 
              loc=lc, 
              fontsize=12 + i * 5, 
              fontweight=weight[i], 
              pad=10 + i * 15)
    
    # Ограничиваем оси от 0 до 1, как на картинке
    plt.xlim(0, 1)
    plt.ylim(0, 1)

# Добавляем нижнюю подпись (фигура 3.12)
# Используем figtext для позиционирования по центру всей фигуры
plt.figtext(0.5, 0.0, 'Рисунок 3.12 — Заголовок графика', 
            ha='center', fontsize=16, fontweight='bold')

# Автоматическое выравнивание
plt.tight_layout(rect=[0, 0.05, 1, 0.95])

plt.show()