from matplotlib import pyplot as plt
import numpy as np
x = np.arange(1,16)

y = x**2
print(x)
print(y)


plt.plot(x,y, color="purple",linestyle='-',marker='o')
plt.subplot(1,2,1)
plt.title("Quadrados dos Primeiros 15 números")
plt.xlabel("Número")
plt.ylabel("Quadrado")
plt.grid(True)
plt.legend
plt.show()

plt.subplot(2,1,2)
plt.subplot(x,y, color="deep ocean blue",linestyle="-",marker='x')
plt.title("Dispersão dos dados aleatórios")
plt.scatter(x,y,color="deep ocean blue")
plt.show()