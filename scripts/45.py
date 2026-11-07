"""
Глава 14. Настройка представления
Управление сценой, заголовком, осями, colorbar и камерой
(Полностью исправленная версия для Plotly)
"""

import numpy as np
import plotly.graph_objects as go

# ============================================
# ДАННЫЕ: 3D спираль (из Главы 13)
# ============================================
t = np.linspace(-5, 5, 100)
x = 3 * np.cos(t)
y = 3 * np.sin(t)
z = t / np.pi

# ============================================
# СОЗДАНИЕ 3D СЦЕНЫ
# ============================================
fig = go.Figure()

# Добавление 3D спирали
fig.add_trace(go.Scatter3d(
    x=x, y=y, z=z,
    mode='lines',
    line=dict(
        width=10,                    # Аналог tube_radius
        color=z,                     # Цвет зависит от Z
        colorscale='Plasma',         # Аналог colormap='plasma'
        colorbar=dict(               # Аналог mlab.colorbar()
            title=dict(
                text='Высота Z',
                font=dict(size=14, color='black')
            ),
            orientation='v',          # 'v' - вертикально, 'h' - горизонтально
            thickness=20,
            len=0.75,
            x=1.02                    # Положение справа
        )
    ),
    name='3D Спираль',
    showlegend=True
))

# ============================================
# 14.1 Управление Фигурой/Сценой
# ============================================
fig.update_layout(
    # Размер сцены (аналог mlab.figure(size=...))
    width=1000,
    height=700,
    
    # Цвет фона сцены (аналог mlab.figure(bgcolor=...))
    paper_bgcolor='rgb(240, 248, 255)',  # Светло-голубой фон
    plot_bgcolor='rgb(255, 255, 255)',   # Белый фон графика
    
    # Заголовок фигуры (аналог mlab.title())
    title=dict(
        text='<b>Глава 14. Настройка представления</b><br>'
             '<sup>3D Спираль с настройками сцены</sup>',
        font=dict(size=20, color='darkblue', family='Arial'),
        x=0.5,
        xanchor='center'
    ),
    
    # Отображение легенды
    showlegend=True,
    legend=dict(
        x=0.02,
        y=0.98,
        bgcolor='rgba(255, 255, 255, 0.8)',
        bordercolor='black',
        borderwidth=1,
        font=dict(size=12, color='black')
    )
)

# ============================================
# 14.2.3 Настройка осей координат
# ============================================
fig.update_layout(
    scene=dict(
        # Настройка оси X
        xaxis=dict(
            title=dict(
                text='Ось X',
                font=dict(size=16, color='red')  # ИСПРАВЛЕНО: titlefont -> title=dict(font=...)
            ),
            showbackground=True,
            backgroundcolor='rgb(245, 245, 245)',
            gridcolor='lightgray',
            gridwidth=1,
            range=[-4, 4],
            showline=True,           # Рамка (outline)
            linewidth=2,
            linecolor='black',
            mirror=True
        ),
        # Настройка оси Y
        yaxis=dict(
            title=dict(
                text='Ось Y',
                font=dict(size=16, color='green')  # ИСПРАВЛЕНО
            ),
            showbackground=True,
            backgroundcolor='rgb(245, 245, 245)',
            gridcolor='lightgray',
            gridwidth=1,
            range=[-4, 4],
            showline=True,           # Рамка (outline)
            linewidth=2,
            linecolor='black',
            mirror=True
        ),
        # Настройка оси Z
        zaxis=dict(
            title=dict(
                text='Ось Z',
                font=dict(size=16, color='blue')  # ИСПРАВЛЕНО
            ),
            showbackground=True,
            backgroundcolor='rgb(245, 245, 245)',
            gridcolor='lightgray',
            gridwidth=1,
            range=[-2, 2],
            showline=True,           # Рамка (outline)
            linewidth=2,
            linecolor='black',
            mirror=True
        ),
    )
)

# ============================================
# 14.3 Управление камерой
# ============================================
fig.update_layout(
    scene=dict(
        camera=dict(
            # Положение камеры (аналог mlab.view())
            eye=dict(x=1.8, y=1.8, z=1.5),   # Позиция камеры
            center=dict(x=0, y=0, z=0),       # Фокус (центр)
            up=dict(x=0, y=0, z=1)            # Направление "вверх"
        ),
        
        # Соотношение сторон
        aspectmode='cube',
        aspectratio=dict(x=1, y=1, z=0.8)
    )
)

# ============================================
# ОТОБРАЖЕНИЕ
# ============================================
fig.show()

print("=" * 70)
print("✅ Глава 14. Настройка представления - ВЫПОЛНЕНА УСПЕШНО!")
print("=" * 70)
print("Реализованные настройки из учебника:")
print("  • 14.1 Управление сценой (размер, фон)")
print("  • 14.2.1 Заголовок сцены")
print("  • 14.2.2 Внешний контур (outline)")
print("  • 14.2.3 Настройка осей координат (подписи, цвета)")
print("  • 14.2.4 Цветовая полоса (colorbar)")
print("  • 14.3 Управление камерой")
print("=" * 70)