from matplotlib import pyplot as plt
import numbpy as np

x = np.arange(-20,21)
y = np.where(x < 0, np.abs(x)**2,
             np.where(x == 0, 0, x**3))

#Criar uma lista x de (-20,21):
#for i in range (-20,21):
#    x.append(i)


#calcular y conforme regras
#y = []
#for num in x:
#    if num == 0:
#       y.append(abs(num) ** 2)
#       elif 