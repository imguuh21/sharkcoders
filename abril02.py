from matplotlib import pyplot as plt
import numpy as np
N1= np.random.normal(0,1,500)
plt.subplot(1,2,1)
plt.title("Histograma-(10 bins)")
H1 = plt.hist(N1,bins=10,color="orange",edgecolor="black")

plt.subplot(1,2,2)
plt.title("Histograma-(50 bins)")
H2 = plt.hist(N1,bins=50,color="teal",edgecolor="black")
plt.tight_layout()
plt.show()