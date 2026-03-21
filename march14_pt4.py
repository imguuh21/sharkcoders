from matplotlib import pyplot as plt
import numpy as np

x = np.arange(-20,21)
y = np.where(x < 0, np.abs(x)**2,
             np.where(x == 0, 0, x**3))
dark_blue = "#040ec7"

plt.plot(x, y, color=dark_blue, linestyle="-", marker='d')
plt.title("Quadrados Negativos")
plt.subplot(1, 3, 1)
plt.xlabel("Quadrados Negativos")
plt.ylabel("Cubos Positivos")
plt.grid(True)
#plt.legend()


plt.subplot(1, 3, 2)
plt.title("Quadrados Negativos")
plt.bar(x,y,color="magenta",edgecolor="black")
plt.xlabel("Quadrados Negativos")
plt.ylabel("Cubos Positivos")
plt.grid(True)
#plt.legend()

cor = "black"
plt.title("Quadrados Negativos")
plt.xlabel("Quadrados Negativos")
plt.ylabel("Cubos Positivos")
plt.subplot(1,3,3)
for i in range(len(x)):
    if x[i] <= 0:
        cor = "red"
    elif x[i] == 0:
        cor = "black"
    else:
        cor = "green"
    plt.scatter(x[i], y[i], color=cor)
plt.tight_layout()
plt.show()

# Criar uma lista x de (-20,21):
# for i in range (-20,21):
#    x.append(i)


# calcular y conforme regras
# y = []
# for num in x:
#    if num == 0:
#       y.append(abs(num) ** 2)
#         elif