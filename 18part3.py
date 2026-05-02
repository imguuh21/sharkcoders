import numpy as np
from matplotlib import pyplot as plt

plt.ion()

valores = []
indices = []

for i in range(100):
    valor = np.random.normal(0,1) #por padrão média = 0, desvio padrão

    if np.random.rand() < 0.05:
        valor += np.random.choice([-10,10])

    valores.append(valor)
    indices.append(i)

    media = np.mean(valores)
    desvio = np.std(valores)

    limites = (media - 3 + desvio,media + 3 * desvio)

    plt.clf()
    plt.title("detectar anomalia")
    plt.xlabel("tempo")
    plt.ylabel("Valores")

    valores_array = np.array(valores)
    outliers = (valores_array < limites[0]) | (valores_array > limites[1])

    plt.plot(indices,valores,color='blue',label='normal')
    plt.scatter(np.array(indices)[outliers],
                valores_array[outliers]
                ,color="red",label="Anomalia")
    plt.legend()
    plt.pause(0.1)
plt.ioff()
plt.show()