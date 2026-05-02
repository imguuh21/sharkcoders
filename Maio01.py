import numpy as np
from matplotlib import pyplot as plt

plt.ion()


valores = []
medio = []
for i in range(100):
    intensidade = np.random.normal(0,1)
    if np.random.rand < 0.05:
        valor = np.random.choice(-50,50)

plt.legend()
plt.ioff()
plt.show()
