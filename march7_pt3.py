import numpy as np

temperaturas = np.random.normal(22,4,1000)


#gerar 1000 valorse de co2 (normal média 400 ppm,desvio de 50 ppm)
co2 = np.random.normal(400,50,1000)


#filtrar medições criticas
condicao_critica = (temperaturas > 28) & (co2 > 450)
temperaturas_criticas = temperaturas[condicao_critica]
co2_criticos = co2[condicao_critica]

quatindade_criticos = len(temperaturas_criticas)
percentagem_criticos = (quatindade_criticos) / len(temperaturas) * 100

#Se Houver casos criticos, calcula média e desvio padrão
if quatindade_criticos > 0:
    media_temp = np.mean(temperaturas_criticas)
    std_temp = np.std(temperaturas_criticas)
    media_co2 = np.mean(co2_criticos)
    std_co2 = np.std(co2_criticos)
else:
    media_temp = std_temp = media_co2 = std_co2 = np.nan


print(f"total de medições:\n{len(temperaturas)}")
print(f"Medicções criticas (Temp > 28º e Co2 > 450ppm):(quatindade_criticos")
print(f"Percentagem de medição critca