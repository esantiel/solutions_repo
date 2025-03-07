# Problem 3
Let’s explore the trajectories of a freely released payload near Earth—a captivating problem that ties together gravitational physics, orbital mechanics, and numerical simulation. Below is a comprehensive response in Markdown format, including a Python script for simulation and visualization, fulfilling all deliverables.

---

# Trajectories of a Freely Released Payload Near Earth

## Motivation
When a payload is released from a rocket near Earth, its subsequent path is shaped by its initial position, velocity, and Earth’s gravitational pull. Depending on these conditions, the trajectory could be elliptical (orbiting), parabolic (just escaping), or hyperbolic (escaping with excess speed). This scenario is fundamental to space mission design, such as deploying satellites, planning reentries, or achieving escape velocities, offering a practical lens into celestial mechanics.



[Simulation](Problem_3.html)


## Task Breakdown

### 1. Analysis of Possible Trajectories

The trajectory type depends on the payload’s specific energy relative to Earth’s gravitational potential:
- **Total Mechanical Energy**: $E = \frac{1}{2} v^2 - \frac{G M}{r}$

  - $E < 0$: Elliptical orbit (bound).
  - $E = 0$: Parabolic trajectory (marginal escape).
  - $E > 0$: Hyperbolic trajectory (unbound, escape).

#### Key Parameters
- $G = 6.67430 \times 10^{-11} \, \text{m}^3 \text{kg}^{-1} \text{s}^{-2}$ (gravitational constant)
- $M = 5.972 \times 10^{24} \, \text{kg}$ (Earth’s mass)
- $r$: Distance from Earth’s center
- $v$: Velocity magnitude
- Escape velocity: $v_{\text{esc}} = \sqrt{\frac{2 G M}{r}}$

- **Elliptical**: $v < v_{\text{esc}}$, payload orbits Earth.
- **Parabolic**: $v = v_{\text{esc}}$, payload escapes to infinity with zero residual speed.
- **Hyperbolic**: $v > v_{\text{esc}}$, payload escapes with excess speed.

### 2. Numerical Analysis

The equations of motion under gravity (two-body problem) are:

$$\ddot{\mathbf{r}} = -\frac{G M}{r^3} \mathbf{r}$$

where $\mathbf{r} = (x, y)$, $r = |\mathbf{r}|$. We’ll solve this numerically using initial conditions:

- **Position**: $\mathbf{r}_0 = (x_0, y_0)$

- **Velocity**: $\mathbf{v}_0 = (v_{x0}, v_{y0})$

### 3. Relation to Space Scenarios
- **Orbital Insertion**: $v < v_{\text{esc}}$ and tangential velocity yields a stable orbit.
- **Reentry**: Low altitude and sub-escape speed with downward component leads to atmospheric entry.
- **Escape**: $v \geq v_{\text{esc}}$ sends the payload away from Earth.

### 4. Computational Tool

#### Python Script
```python
import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # m^3 kg^-1 s^-2
M = 5.972e24     # kg (Earth mass)
R_earth = 6.371e6  # m (Earth radius)

# Gravitational acceleration
def gravity(r):
    r_mag = np.sqrt(r[0]**2 + r[1]**2)
    return -G * M / r_mag**3 * r

# Derivative function for ODE
def deriv(state, t):
    x, y, vx, vy = state
    r = np.array([x, y])
    ax, ay = gravity(r)
    return [vx, vy, ax, ay]

# RK4 solver
def rk4_step(state, t, dt):
    k1 = np.array(deriv(state, t))
    k2 = np.array(deriv(state + 0.5 * dt * k1, t + 0.5 * dt))
    k3 = np.array(deriv(state + 0.5 * dt * k2, t + 0.5 * dt))
    k4 = np.array(deriv(state + dt * k3, t + dt))
    return state + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

# Simulation parameters
dt = 10  # seconds
t_max = 20000  # seconds
t = np.arange(0, t_max, dt)

# Initial conditions (altitude 200 km, various velocities)
h = 200e3  # m
r0 = R_earth + h
v_esc = np.sqrt(2 * G * M / r0)  # escape velocity at r0

scenarios = [
    {"name": "Elliptical (Orbit)", "v0": [0, 0.9 * v_esc / np.sqrt(2)], "color": "blue"},
    {"name": "Parabolic (Escape)", "v0": [0, v_esc], "color": "green"},
    {"name": "Hyperbolic (Fast Escape)", "v0": [0, 1.2 * v_esc], "color": "red"}
]

# Simulate trajectories
trajectories = []
for scenario in scenarios:
    state = [r0, 0, scenario["v0"][0], scenario["v0"][1]]  # [x, y, vx, vy]
    path = [state[:2]]
    for ti in t[1:]:
        state = rk4_step(state, ti, dt)
        path.append(state[:2])
        if np.sqrt(state[0]**2 + state[1]**2) > 5 * R_earth:  # stop if far away
            break
    trajectories.append(np.array(path))

# Visualization
plt.figure(figsize=(12, 8))

# Earth
theta = np.linspace(0, 2 * np.pi, 100)
x_earth = R_earth * np.cos(theta)
y_earth = R_earth * np.sin(theta)
plt.fill(x_earth, y_earth, "lightblue", label="Earth")

# Trajectories
for i, traj in enumerate(trajectories):
    plt.plot(traj[:, 0], traj[:, 1], label=scenarios[i]["name"], color=scenarios[i]["color"])

plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.title("Trajectories of a Payload Released Near Earth (200 km Altitude)")
plt.legend()
plt.axis("equal")
plt.grid(True)
plt.show()

# Energy check
for scenario in scenarios:
    v0 = np.sqrt(scenario["v0"][0]**2 + scenario["v0"][1]**2)
    E = 0.5 * v0**2 - G * M / r0
    print(f"{scenario['name']}: Specific Energy = {E:.2e} J/kg")
```

#### Output
- **Elliptical**: $v = 0.9 v_{\text{esc}} / \sqrt{2} \approx 7.8 \, \text{km/s}$, $E < 0$

- **Parabolic**: $v = v_{\text{esc}} \approx 11.0 \, \text{km/s}$, $E = 0$

- **Hyperbolic**: $v = 1.2 v_{\text{esc}} \approx 13.2 \, \text{km/s}$, $E > 0$

---

## Deliverables

### Explanation
- **Trajectories**: Determined by energy: elliptical (bound), parabolic (marginal escape), hyperbolic (unbound).
- **Numerical Method**: RK4 integrates the two-body problem, tracking position and velocity.
- **Scenarios**: Orbital insertion (elliptical), reentry (if aimed downward), escape (parabolic/hyperbolic).

### Graphical Representation
- Plot shows Earth with three trajectories from 200 km altitude:
  - Blue: Elliptical orbit.
  - Green: Parabolic escape.
  - Red: Hyperbolic escape.

---

## Discussion
The simulation captures key dynamics:
- **Orbital Insertion**: Tangential $v < v_{\text{esc}}$ yields stable orbits (e.g., satellites).
- **Reentry**: Downward velocity at low altitude (not simulated here) leads to atmospheric capture.
- **Escape**: $v \geq v_{\text{esc}}$ sends payloads beyond Earth’s influence, critical for lunar or interplanetary missions.

Limitations include ignoring atmospheric drag, Earth’s oblateness, and other bodies. Adding these or varying initial directions could enhance realism.

Let me know if you’d like an HTML version or further refinements!