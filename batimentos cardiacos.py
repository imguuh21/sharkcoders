import numpy as np
from matplotlib import pyplot as plt
plt.ion()

tempos = np.array([])
batimentos = np.array([])
I = 75

for segundo in range(150):
    bpm = np.random.normal(75, 5)

    if np.random.rand() <= 0.2:
        bpm += 60

    tempo = np.append(tempos, segundo)
    batimetos = np.append(batimentos, bpm)

    anomalia = batimetos > 120

    plt.clf()
    plt.title("Batimentos Cardíacos")
    plt.xlabel("Tempo (s)")
    plt.ylabel("BPM")

    plt.plot(tempos,batimentos,color="green",label="bpms")
    plt.scatter(tempos[anomalia],batimentos[anomalia],color="red",label="Anomalia")
    plt.axhline(120,color="black",linestyle="--",linewidth="1")
    plt.legend()
    plt.grid(True)
    plt.pause(0.2)
plt.ioff()
plt.show()