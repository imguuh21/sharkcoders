from matplotlib import pyplot as plt
import numpy as np

plt.subplot(1,2,1) #linhas,colunas, indice
plt.plot([1,2,3],[1,4,9])
plt.title("Primeiro Gráico")

plt.subplot(1,2,2)
plt.plot([1,2, 3],[9,4,1])
plt.title("Segundo Gráfico")

plt.subplot(1,3,3)
plt.plot([1,2,3],[10,8,3])
plt.title("Terceiro Gráfico")

plt.tight_layout()
plt.show()