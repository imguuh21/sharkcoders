import numpy as np
from matplotlib import pyplot as plt

plt.ion()#atualiza o grafico
#dados linha 6 a linha 22
tempo = np.array([])
sinais = np.array([])

N = 120

for i in range(300):
    t = i * 0.5
    sinal = np.random.normal(-50,10)#média -50 variação 10

    tempo = np.append(tempo,t)
    sinais = np.append(sinais, sinal)

    if len(tempo) > N:
        tempo = tempo[-N:len(tempo):1]
        sinais = sinais[-N:len(sinais):1]

    fracos = sinais < -70

    plt.clf()#clear frame
    plt.title("intensidade do Sinal")
    plt.xlabel("Tempo em Segundos")
    plt.ylabel("Intensidade (dBm)")

    plt.plot(tempo,sinais,  label="Intesidade do sinal",color="blue")
    plt.scatter(tempo[fracos],sinais[fracos],color="red")
    plt.axhline(-70,color="black",linestyle="--",linewidth=1)
    plt.legend()
    plt.grid(True)
    plt.pause(0.2)


plt.ioff()
plt.show()