from matplotlib import pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2, color="coral")

max_points = 100
x_data = np.array([])
y_data = np.array([])
time_step = 0

ax.set_ylim(-1.5, 1.5)
ax.set_xlim(10, max_points)
ax.set_ylabel("Tempo")
ax.set_xlabel("Seno(t)")
ax.set_title("Gráfico Sinusoidal em Tempo Real")
ax.grid(True, alpha=0.3)

def update(frame):
    global x_data, y_data, time_step

    y_new = np.sin(time_step * 0.1)

    x_data = np.append(x_data, time_step)
    y_data = np.append(y_data,y_new)

    if len(x_data) > max_points:
        x_data = x_data[-max_points:]
        y_data = y_data[-max_points:]
    line.set_data(x_data,y_data)
    ax.set_xlim(time_step - max_points, time_step)
    time_step += 1
    return line,

anim = animation.FuncAnimation(fig, update,
                       interval=100,  # Atualiza a cada 100ms
                       frames=1000)   # Total de quadros

plt.tight_layout()
plt.show()