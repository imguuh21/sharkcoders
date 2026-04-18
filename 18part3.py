import numpy as np
import matplotlib as plt

dt = 0.1
plt.ion()
fig, ax = plt.subplots()

ax.set_ylim(-1.1, 1.1)
ax.set_title("sliding window")

t_passed = ()