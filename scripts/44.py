"""
Глава 13. Быстрый старт
Визуализация 3D спирали (учебник стр. 326-327)
"""

import numpy as np
import plotly.graph_objects as go

# Данные из учебника
t = np.linspace(-5, 5, 100)
x = 3 * np.cos(t)
y = 3 * np.sin(t)
z = t / np.pi

# Построение 3D спирали
fig = go.Figure(data=go.Scatter3d(
    x=x, y=y, z=z,
    mode='lines',
    line=dict(
        width=8,
        color=z,
        colorscale='Plasma',
        colorbar=dict(title='Высота Z')
    )
))

# Настройка сцены
fig.update_layout(
    title='Глава 13. Быстрый старт (3D Спираль)',
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z'
    ),
    width=900,
    height=700
)

fig.show()
print("✅ Глава 13 успешно выполнена!")