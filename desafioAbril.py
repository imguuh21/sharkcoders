from matplotlib import pyplot as plt
import numpy as np

N3 = np.random.normal(2,1,600)
x = np.arange(10)
y = x**2
N4 = np.random.rand(150)


fig, (ax1, ax2,ax3) = plt.subplots(1, 3, figsize=(10, 4))

#Gráfico 1
ax1.hist(N3, bins=25, color="coral", edgecolor="gray")
ax1.set_title("Histograma Normal")

#Gráfico 2
ax2.bar(x, y, color="navy")
ax2.set_title("Potências de 2")

#Gráfico 3
ax3.scatter(N4,color="lime green",)
ax3.set_title("Scatter aleatório")
plt.tight_layout()
plt.show()