import numpy as np
from mayavi import mlab

mlab.figure(bgcolor=(0.1, 0.1, 0.1), size=(600, 700))

# 1. ОРТАЛЫҚ БӨЛІК (Цилиндр)
u_c = np.linspace(0, 2*np.pi, 50)
v_c = np.linspace(0, 3.5, 50)
U_c, V_c = np.meshgrid(u_c, v_c)
x_c = 0.5 * np.cos(U_c)
y_c = 0.5 * np.sin(U_c)
z_c = V_c
mlab.mesh(x_c, y_c, z_c, color=(0.7, 0.4, 0.3))

# 2. ЖОҒАРҒЫ БӨЛІК (Басы - жарты сфера)
p_t, t_t = np.mgrid[0:np.pi/2:30j, 0:2*np.pi:30j]
x_t = 0.55 * np.sin(p_t) * np.cos(t_t)
y_t = 0.55 * np.sin(p_t) * np.sin(t_t)
z_t = 0.55 * np.cos(p_t) + 3.5
mlab.mesh(x_t, y_t, z_t, color=(0.8, 0.3, 0.3))

# 3. АСТЫНДАҒЫ ЕКІ ШАРИК (Сфералар)
phi, theta = np.mgrid[0:np.pi:30j, 0:2*np.pi:30j]

# Сол жақтағы шарик (центрі: -0.7, 0, 0)
x_s1 = 0.7 * np.sin(phi) * np.cos(theta) - 0.7
y_s1 = 0.7 * np.sin(phi) * np.sin(theta)
z_s1 = 0.7 * np.cos(phi)
mlab.mesh(x_s1, y_s1, z_s1, color=(0.6, 0.3, 0.2))

# Оң жақтағы шарик (центрі: 0.7, 0, 0)
x_s2 = 0.7 * np.sin(phi) * np.cos(theta) + 0.7
y_s2 = 0.7 * np.sin(phi) * np.sin(theta)
z_s2 = 0.7 * np.cos(phi)
mlab.mesh(x_s2, y_s2, z_s2, color=(0.6, 0.3, 0.2))

# 4. ШАРИКТЕРДЕГІ "ШӨП" (Палкалар - Quiver3d)
# Сфера бетіндегі нүктелерді сиректеу етіп аламыз
phi_h, theta_h = np.mgrid[0:np.pi:10j, 0:2*np.pi:10j]

# Бірінші шариктің "шөбі"
xh1 = (0.7 * np.sin(phi_h) * np.cos(theta_h) - 0.7).flatten()
yh1 = (0.7 * np.sin(phi_h) * np.sin(theta_h)).flatten()
zh1 = (0.7 * np.cos(phi_h)).flatten()

# Екінші шариктің "шөбі"
xh2 = (0.7 * np.sin(phi_h) * np.cos(theta_h) + 0.7).flatten()
yh2 = (0.7 * np.sin(phi_h) * np.sin(theta_h)).flatten()
zh2 = (0.7 * np.cos(phi_h)).flatten()

# Барлық нүктелерді біріктіру
X = np.concatenate([xh1, xh2])
Y = np.concatenate([yh1, yh2])
Z = np.concatenate([zh1, zh2])

# Бағыттар (Центрден сыртқа қарай)
U = np.concatenate([(xh1 + 0.7), (xh2 - 0.7)])
V = np.concatenate([yh1, yh2])
W = np.concatenate([zh1, zh2])

# "Шөптің" ұзындығын реттеу
length = 0.4
U, V, W = U * length, V * length, W * length

# Векторларды салу (AssertionError болмас үшін массивтер қолданылды)
mlab.quiver3d(X, Y, Z, U, V, W, mode='2ddash', color=(0.2, 0.6, 0.2), line_width=3.0)

mlab.title("Topological Math Model: 14-15 Chapters")
mlab.show()