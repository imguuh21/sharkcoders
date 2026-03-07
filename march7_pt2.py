import numpy as np

temperaturas = np.random.normal(20,5,365)
dias_quentes = temperaturas[temperaturas > 30]

percentagem = (len(dias_quentes)) / len(temperaturas) * 100

print(f"Dias com >30ºC:\n{len(dias_quentes)}")
print(f"Percentagem de dias muito quentes:\n{percentagem:.2f}%")