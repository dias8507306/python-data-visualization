import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5), facecolor='#f0f0f0')

plt.suptitle('PROJECT BY DIAS', fontsize=20, fontweight='bold', color='darkblue')

# --- ГРАФИК С АННОТАЦИЕЙ ---
plt.subplot(111) 
plt.title('Custom Annotation Style', fontsize=14, pad=20)

# Рисуем пустой график с границами
plt.xlim(0, 1)
plt.ylim(0, 1)

# Твоя кастомная аннотация
plt.annotate(
    'ДИАС', 
    xy=(0.2, 0.4),      # Куда указывает стрелка
    xytext=(0.6, 0.8),  # Где твое имя
    fontsize=25,        # Размер имени
    fontweight='bold',  # Жирный шрифт
    color='white',      # Цвет текста
    # Добавляем красивую рамку вокруг имени
    bbox=dict(boxstyle="round,pad=0.5", fc="crimson", ec="black", lw=2),
    # Настраиваем крутую стрелку
    arrowprops=dict(
        arrowstyle="fancy", # Стиль стрелки "фантазийный"
        connectionstyle="arc3,rad=-0.3", # Делаем стрелку изогнутой
        facecolor="gold",   # Золотой цвет стрелки
        edgecolor="black",  # Черный контур
        shrinkA=5,          # Отступ от текста
        shrinkB=5           # Отступ от точки
    )
)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()