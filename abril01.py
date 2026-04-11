from matplotlib import pyplot as plt
import numpy as np

numeros = np.random.normal(0,1,1000)
plt.subplot(2,1,1)
plt.title("Histograma-Distribuição normal")
plt.hist(numeros, bins=30,density=True,color="skyblue",edgecolor="black")


x =np.random.normal(0,1,100)#rand(100)tbm funciona
y =np.random.normal(0,1,100)


plt.subplot(2,1,2)
plt.scatter(x,y,color="red")
plt.title("Scatter por Número aleatório")
plt.xlabel("X")
plt.ylabel("Y")
plt.tight_layout()
plt.show()