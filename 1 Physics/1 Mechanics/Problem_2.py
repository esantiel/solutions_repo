import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation, PillowWriter

# Sarkaç parametreleri
g = 9.8      # yerçekimi (m/s^2)
L = 1.0      # uzunluk (m)
omega0 = np.sqrt(g / L)  # doğal frekans

# Sistem dinamikleri
def pendulum_deriv(state, t, gamma, f, omega):
    theta, v = state
    dtheta_dt = v
    dv_dt = -omega0**2 * np.sin(theta) - gamma * v + f * np.cos(omega * t)
    return [dtheta_dt, dv_dt]

# Simülasyon parametreleri
t = np.linspace(0, 10, 500)  # GIF için kısa zaman (10s, 500 kare)
initial_conditions = [0.1, 0]  # [theta0, v0]

# İncelenecek durumlar
cases = [
    {"gamma": 0.1, "f": 0.5, "omega": omega0, "label": "Rezonans"},
    {"gamma": 0.5, "f": 1.2, "omega": 1.5, "label": "Orta Düzey Zorlama"},
    {"gamma": 0.2, "f": 2.5, "omega": 1.2, "label": "Kaotik"}
]

# Tüm durumlar için yörünge simülasyonu
trajectories = []
for case in cases:
    sol = odeint(pendulum_deriv, initial_conditions, t, args=(case["gamma"], case["f"], case["omega"]))
    theta = sol[:, 0]
    trajectories.append(theta)

# Animasyon kurulumu
fig, axs = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
lines = []
for i, ax in enumerate(axs):
    # Sarkaç pivotu (0, 0), kütle (x, y)
    line, = ax.plot([], [], 'o-', lw=2, markersize=10)  # Kütle ile çizgi
    lines.append(line)
    ax.set_xlim(-1.5*L, 1.5*L)
    ax.set_ylim(-1.5*L, 0.5*L)
    ax.set_title(cases[i]["label"])
    ax.set_xlabel('X (m)')
    if i == 0:
        ax.set_ylabel('Y (m)')
    ax.grid(True)
    # Pivot noktası ekle
    ax.plot([0], [0], 'ko', markersize=5)

# Başlangıç fonksiyonu
def init():
    for line in lines:
        line.set_data([], [])
    return lines

# Animasyon fonksiyonu
def animate(frame):
    for i, theta in enumerate([traj[frame] for traj in trajectories]):
        x = L * np.sin(theta)
        y = -L * np.cos(theta)
        lines[i].set_data([0, x], [0, y])
    return lines

# Animasyon oluştur
ani = FuncAnimation(fig, animate, frames=len(t), init_func=init, blit=True, interval=20)

# GIF olarak kaydet
writer = PillowWriter(fps=25)
ani.save("sarkaç_hareketi.gif", writer=writer)

plt.tight_layout()
plt.show()