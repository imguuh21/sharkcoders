import numpy as np

a = np.array([4, 7, 2, 9, 1, 6])
#1)ve q é numpy
#2) [F, T, F, T, F,T]
#3) "=" [4,99,2,99,1,99 ]
a[a > 5] = 99
a[a < 3] = 0