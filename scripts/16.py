import matplotlib.pyplot as plt


conn_style = [
    'angle,angleA=90,angleB=0,rad=0.0',
    'angle3,angleA=90,angleB=0',
    'arc,angleA=0,angleB=0,armA=0,armB=40,rad=0.0',
    'arc3,rad=-1.0',
    'bar,armA=0.0,armB=0.0,fraction=0.1,angle=70',
    'bar,fraction=-0.5,angle=180',
]

# Создаем сетку 2x3
fig, axs = plt.subplots(2, 3, figsize=(12, 8))
plt.suptitle('АРСЕНАЛ ИЗОГНУТЫХ СТРЕЛОК ДИАСА', fontsize=20, fontweight='bold', color='darkgreen')

for i in range(2):
    for j in range(3):
        idx = i * 3 + j
        ax = axs[i, j]
        
        # Выводим описание стиля внутри каждого графика
        ax.text(0.05, 0.5, '\n'.join(conn_style[idx].split(',')), 
                fontsize=9, bbox=dict(boxstyle="round", fc="white", ec="gray", alpha=0.8))
        
        # Рисуем аннотацию с именем ДИАС и разными стилями изгиба
        ax.annotate(
            'ДИАС', 
            xy=(0.2, 0.2),      # Куда указывает стрелка
            xytext=(0.7, 0.8),  # Откуда идет текст
            fontsize=12,
            fontweight='bold',
            color='white',
            bbox=dict(boxstyle="round,pad=0.3", fc="tomato", ec="black"), # Красивая рамка для имени
            arrowprops=dict(
                arrowstyle='-|>', 
                connectionstyle=conn_style[idx],
                color='black',
                lw=2
            )
        )
        
        # Настройка осей (от 0 до 1)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)


plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()