import numpy as np


#2 arrays de 0,100 quatidade 100
#soma dos dois
#desvio padrão

array_1 = np.random.randint(1,100,50)
array_2 = np.random.randint(1,100,50)

soma = array_1 + array_2
print(array_1)
print(array_2)
print(soma)

std_a = np.std(soma)
print(std_a)