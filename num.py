import numpy as np

#crair um array NumPY
a = np.array([1, 2, 3, 4])

print(a) #[1 2 3 4)

b = a * 2

print(b) #[2 4 6 8]
#matriz 2D

m = np.array([[1,2], [3, 4]])

print(m)
# [[1 2]
#  [3 4]]

#algumas funções uteis
print(np.mean(a)) #média -> 2.5
print(np.sum(a))  #Soma -> 10
print(np.sqrt(a)) #raiz quadrada -> 1.41421356 1.73205081 2.