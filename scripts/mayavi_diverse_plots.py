import numpy as np
from mayavi import mlab

def create_final_diverse_plots():
    print("37 мүлдем әртүрлі график дайындалуда... Күте тұрыңыз.")

    # 1-8: 14-ТАРАУ. КҮРДЕЛІ МАТЕМАТИКАЛЫҚ ПІШІНДЕР (MESH)
    # Бұл жерде тригонометриялық "суперформулалар" қолданылады
    for i in range(1, 9):
        mlab.figure(i, bgcolor=(0, 0, 0), size=(300, 300))
        phi, theta = np.mgrid[0:np.pi:30j, 0:2*np.pi:30j]
        r = 0.5 + np.sin(i * phi) * np.cos(i * theta)
        x, y, z = r*np.sin(phi)*np.cos(theta), r*np.sin(phi)*np.sin(theta), r*np.cos(phi)
        mlab.mesh(x, y, z, colormap='magma', representation=['surface', 'wireframe'][i%2])
        mlab.title(f"3D Shape {i}")

    # 9-16: 15.2-бөлім. ВЕКТОРЛЫҚ ҚҰЙЫНДАР (QUIVER3D)
    # Математикалық құйын, жарылыс және толқын түрлері
    for i in range(9, 17):
        mlab.figure(i, bgcolor=(0.05, 0.05, 0.1), size=(300, 300))
        x, y, z = np.mgrid[-2:2:5j, -2:2:5j, -2:2:5j]
        if i == 9: u, v, w = -y, x, z*0.1 # Vortex (Құйын)
        elif i == 10: u, v, w = x, y, z   # Explosion (Жарылыс)
        else: u, v, w = np.sin(x*i), np.cos(y*i), np.cos(z)
        mlab.quiver3d(x, y, z, u, v, w, mode=['arrow', 'cone', 'cylinder'][i%3], scale_factor=0.5)
        mlab.title(f"Vector {i}")

    # 17-24: 14.5-бөлім. КӨЛЕМДІ ИЗОБЕТКЕЙЛЕР (CONTOUR3D)
    # Нысанның ішкі қабаттары (Томография сияқты)
    for i in range(17, 25):
        mlab.figure(i, bgcolor=(0, 0.05, 0), size=(300, 300))
        x, y, z = np.ogrid[-2:2:25j, -2:2:25j, -2:2:25j]
        scalars = np.sin(x*i/3) + np.cos(y*i/3) + np.sin(z*i/3)
        mlab.contour3d(scalars, contours=3, transparent=True, opacity=0.4)
        mlab.title(f"Volume {i}")

    # 25-30: 15.1-бөлім. БАҒАНАЛЫ ГРАФИКТЕР (BARCHART)
    # 3D статистикалық бағаналар
    for i in range(25, 31):
        mlab.figure(i, bgcolor=(0.1, 0, 0.1), size=(300, 300))
        x, y = np.mgrid[0:4, 0:4]
        z = np.random.uniform(1, i-20, size=x.shape)
        mlab.barchart(x, y, z, colormap='cool')
        mlab.title(f"Bar {i}")

    # 31-35: 15.4-бөлім. КЕҢІСТІКТЕГІ ТРАЕКТОРИЯЛАР (PLOT3D)
    # Спиральдар мен күрделі жіптер
    for i in range(31, 36):
        mlab.figure(i, bgcolor=(0, 0, 0), size=(300, 300))
        t = np.linspace(0, 10*np.pi, 400)
        x, y, z = np.sin(t*(i-30)), np.cos(t), t/15
        mlab.plot3d(x, y, z, t, tube_radius=0.04, colormap='Spectral')
        mlab.title(f"Path {i}")

    # 36-37: НҮКТЕЛЕР ЖӘНЕ ЖАЙЫЛЫМ (POINTS3D)
    for i in range(36, 38):
        mlab.figure(i, bgcolor=(0.1, 0.1, 0), size=(300, 300))
        x, y, z = np.random.normal(0, 1, 100), np.random.normal(0, 1, 100), np.random.normal(0, 1, 100)
        mlab.points3d(x, y, z, mode=['sphere', 'cube'][i-36], scale_factor=0.15, color=(1, 0.5, 0))
        mlab.title(f"Points {i}")

    print("Барлық 37 бірегей график дайын!")
    mlab.show()

create_final_diverse_plots()