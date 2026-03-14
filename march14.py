from matplotlib import pyplot as plt
import numpy as np
#1 criar um array com 100 numeros aleatórios etre 0 e 50
dados = np.random.uniform(0,50,100)
#2 Criar Histogramas
plt.subplot(2,1,1)
plt.hist(dados, bins=10,color="skyblue",edgecolor="black")
plt.title("Histograma dos Dados  Aleatórios")
plt.xlabel("Valor")
plt.ylabel("Frequência")

#3 criar gráfico de dispersão (scatter plot)

indices = np.arange(len(dados))

plt.subplot(2,1,2)

plt.scatter(indices,dados,color="purple")
plt.title("Dispersão dos Dados Aleatórios")
plt.xlabel("índice")
plt.ylabel("Valor")

plt.tight_layout()

plt.show()