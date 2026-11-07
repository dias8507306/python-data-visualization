import matplotlib.pyplot as plt

# 1. Мәліметтерді дайындау
vals = [24, 17, 53, 21, 35]
# Суреттегідей болуы үшін 'BMW'-ны 'BMV' деп өзгертсеңіз болады
labels = ['Ford', 'Toyota', 'BMV', 'AUDI', 'Jaguar'] 

# 2. Графикті құру
fig, ax = plt.subplots()
ax.pie(vals, labels=labels)

# Графиктің дөңгелек пішінін сақтау (созылып кетпеуі үшін)
ax.axis('equal') 

# 3. Көрсету
plt.show()