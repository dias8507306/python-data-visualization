import matplotlib.pyplot as plt

x = [2, 6, 10, 14, 18]
y1 = [3, 9, 2, 7, 10]    
y2 = [5, 4, 1, 10, 12]   
y3 = [10, 2, 8, 4, 6]    

plt.figure(figsize=(8, 6))

plt.plot(x, y1, 'o-r', label='line 1')      
plt.plot(x, y2, 's--g', label='line 2')     
plt.plot(x, y3, '^-.b', label='line 3')     

plt.legend(
    title='Легенда',          
    fontsize=12,             
    facecolor='y',            
    edgecolor='r',            
    framealpha=1,             
    shadow=True,              
    loc='upper left'         
)

plt.title("Бапталған легенда және жаңа мәліметтер")
plt.grid(True, alpha=0.2)
plt.show()