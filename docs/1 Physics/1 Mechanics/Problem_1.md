# Problem 1

### 1. Theoretical Foundation

Projectile motion is a classic two-dimensional problem governed by Newton’s laws under constant gravitational acceleration. Let’s derive the equations from first principles.

#### Deriving the Equations of Motion
Assume a projectile is launched from the origin (x₀ = 0, y₀ = 0) with an initial velocity $v_0$ at an angle $\theta$ above the horizontal, and the only force acting is gravity (acceleration $g$ downward). We’ll neglect air resistance for now.

Break the initial velocity into components:

- Horizontal: $v_{0x} = v_0 \cos\theta$
- Vertical: $v_{0y} = v_0 \sin\theta$

The acceleration due to gravity acts only in the vertical direction:

- $a_x = 0$
- $a_y = -g$

Using kinematics (or integrating the accelerations), the velocity and position as functions of time $t$ are:
- Horizontal:

  - $v_x(t) = v_{0x} = v_0 \cos\theta$ (constant, since $a_x = 0$)
  - $x(t) = v_{0x} t = v_0 \cos\theta \cdot t$

- Vertical:

  - $v_y(t) = v_{0y} + a_y t = v_0 \sin\theta - g t$
  - $y(t) = v_{0y} t + \frac{1}{2} a_y t^2 = v_0 \sin\theta \cdot t - \frac{1}{2} g t^2$

These are parametric equations describing a parabolic trajectory. The family of solutions emerges from varying $v_0$, $\theta$, and $g$. For instance, a higher $v_0$ stretches the parabola, while a larger $g$ compresses it vertically.


---
[Simulation](Problem_1.html)
---


### 2. Analysis of the Range

The range $R$ is the horizontal distance traveled when the projectile returns to $y = 0$ (assuming launch and landing at the same height).

#### Time of Flight
Set $y(t) = 0$ to find the time when the projectile hits the ground:

$$0 = v_0 \sin\theta \cdot t - \frac{1}{2} g t^2$$

Factor out $t$:

$$t (v_0 \sin\theta - \frac{1}{2} g t) = 0$$

Solutions:

- $t = 0$ (launch)
- $t = \frac{2 v_0 \sin\theta}{g}$ (landing)

This $t = \frac{2 v_0 \sin\theta}{g}$ is the time of flight.

#### Range Equation
Substitute into the horizontal position:

$$R = x(t) = v_0 \cos\theta \cdot \frac{2 v_0 \sin\theta}{g}$$

Using the identity $2 \sin\theta \cos\theta = \sin 2\theta$:

$$R = \frac{v_0^2 \sin 2\theta}{g}$$

#### Dependence on Angle
- **Maximum Range**: $R$ is maximized when $\sin 2\theta = 1$, so $2\theta = 90^\circ$, or $\theta = 45^\circ$. Then:

  $$R_{\text{max}} = \frac{v_0^2}{g}$$

- **Symmetry**: $R(\theta) = R(90^\circ - \theta)$, since $\sin 2(90^\circ - \theta) = \sin (180^\circ - 2\theta) = \sin 2\theta$. E.g., ranges at 30° and 60° are equal.
- **Extremes**: At $\theta = 0^\circ$ or $90^\circ$, $\sin 2\theta = 0$, so $R = 0$.

#### Other Parameters
- **Initial Velocity ($v_0$)**: Range scales with $v_0^2$, so doubling $v_0$ quadruples $R$.
- **Gravity ($g$)**: Range is inversely proportional to $g$. On the Moon ($g \approx 1.62 \, \text{m/s}^2$), range is about 6 times that on Earth ($g \approx 9.8 \, \text{m/s}^2$).

---

### 3. Practical Applications

This model simplifies real-world scenarios but can be adapted:
- **Uneven Terrain**: If launched from height $h$, the time to reach $y = -h$ changes. Solve:
  $$-h = v_0 \sin\theta \cdot t - \frac{1}{2} g t^2$$
  This quadratic in $t$ adjusts the range, often increasing it for downward slopes.
- **Air Resistance**: Introduces a drag force proportional to velocity (or its square), requiring numerical solutions. Range typically decreases, and the optimal angle shifts below 45°.
- **Examples**:
  - **Sports**: A soccer ball’s range depends on kick angle and speed, modified by spin and air effects.
  - **Artillery**: Cannons adjust angles for range, accounting for wind and elevation.
  - **Space**: Rockets use initial angles, but thrust and gravity variations dominate.
---
#### Visualization Insights
- For $v_0 = 20 \, \text{m/s}$, $g = 9.8 \, \text{m/s}^2$, the plot shows a peak at 45°, with $R_{\text{max}} \approx 40.8 \, \text{m}$.

- Try $v_0 = 40 \, \text{m/s}$ or $g = 1.62 \, \text{m/s}^2$ to see scaling effects.

#### Extensions
- Add a loop to plot multiple $v_0$ or $g$ values.
- Simulate trajectories $(x(t), y(t))$ parametrically for selected angles.

---

### Conclusion
The range’s dependence on $\theta$ via $\sin 2\theta$ is both elegant and practical, peaking at 45° under ideal conditions. Variations in $v_0$ and $g$ amplify or shrink this relationship, while real-world factors like height or drag enrich the problem. This blend of theory, analysis, and simulation makes projectile motion a timeless physics gem.

