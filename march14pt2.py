from matplotlib import pyplot as plt

valores = (1, 4, 9, 16, 25)
indices = [0, 1, 2, 3, 4]
plt.plot(indices,valores,color="green")
plt.title("Gráfico de Linha")
plt.xlabel("índice")
plt.ylabel("Valor")
plt.tight_layout()

plt.show()