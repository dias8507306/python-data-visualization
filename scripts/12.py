import matplotlib.pyplot as plt

# Создаем сетку 2x3
fig, axs = plt.subplots(2, 3, figsize=(12, 7))

# Список стилей соединительных линий
conn_style = [
    'angle,angleA=90,angleB=0,rad=0.0',
    'angle3,angleA=90,angleB=0',
    'arc,angleA=0,angleB=0,armA=0,armB=40,rad=0.0',
    'arc3,rad=-1.0',
    'bar,armA=0.0,armB=0.0,fraction=0.1,angle=70',
    'bar,fraction=-0.5,angle=180',
]

# Заполняем каждый подграфик
for i in range(2):
    for j in range(3):
        # Текущий индекс стиля в списке
        idx = i * 3 + j
        
        # Отображаем название стиля в левой части графика
        # Разделяем строку по запятым для переноса строк
        axs[i, j].text(0.1, 0.6, '\n'.join(conn_style[idx].split(',')), 
                       fontsize=10, verticalalignment='center')
        
        # Добавляем аннотацию со специфическим стилем линии
        axs[i, j].annotate(
            'text', 
            xy=(0.2, 0.2),      # Координата острия стрелки
            xytext=(0.7, 0.8),  # Координата текста
            arrowprops=dict(
                arrowstyle='->', 
                connectionstyle=conn_style[idx] # Применяем стиль из списка
            )
        )
        
        # Устанавливаем лимиты осей для единообразия
        axs[i, j].set_xlim(0, 1)
        axs[i, j].set_ylim(0, 1)

plt.tight_layout()
plt.show()