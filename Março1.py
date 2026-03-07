import numpy as np

dados = np.random.normal(5,2,500)
dados_filtrados = dados[dados > 7]
print(f"Array filtrado:\n{dados_filtrados}")
print(f"Quantidade de valores > 7: {len(dados_filtrados)}")