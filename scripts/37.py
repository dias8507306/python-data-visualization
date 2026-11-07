import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("mpg")
sns.set_style("whitegrid")

plt.figure(figsize=(10, 6))

# Графикті сызамыз
scatter = sns.scatterplot(
    x="horsepower", 
    y="acceleration", 
    hue="origin",    
    size="weight",    
    sizes=(20, 200), 
    alpha=0.7,
    data=data
)

# --- ЛЕГЕНДАНЫ ЕКІГЕ БӨЛУ ---

# 1. Қазіргі біріккен легенданы алып тастаймыз
plt.gca().get_legend().remove()

# 2. "Origin" (түстер) үшін бөлек легенда қосамыз
# Мұнда тек алғашқы 3 элементті аламыз (usa, japan, europe)
handles, labels = scatter.get_legend_handles_labels()
first_legend = plt.legend(
    handles=handles[1:4], 
    labels=labels[1:4], 
    title="Origin (Шығу тегі)", 
    loc="upper right",
    bbox_to_anchor=(1.15, 1) # Графиктің сыртына шығару үшін
)

# 3. "Weight" (салмақ) үшін бөлек легенда қосамыз
# Алдыңғы легенда өшіп кетпеуі үшін оны қолмен қосамыз
plt.gca().add_artist(first_legend)

second_legend = plt.legend(
    handles=handles[5:], 
    labels=labels[5:], 
    title="Weight (Салмақ)", 
    loc="lower right",
    bbox_to_anchor=(1.15, 0.1)
)

plt.title("Связь мощности и ускорения")
plt.show()