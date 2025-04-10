# Problem 2


# Escape Velocities and Cosmic Velocities


Escape velocity is the minimum speed an object must achieve to break free from a celestial body’s gravitational pull without further propulsion. Building on this, cosmic velocities—first, second, and third—define critical thresholds for orbiting a planet, escaping its gravity, and exiting a star system, respectively. These ideas are the backbone of space exploration, guiding everything from satellite launches to interplanetary missions and dreams of interstellar voyages.


![alt text](41467_2022_32299_Fig4_HTML.png)

## Task Breakdown

### 1. Definitions and Physical Meaning

- **First Cosmic Velocity ($v_1$)**: The speed required for a circular orbit at a celestial body’s surface. It balances gravitational pull with centripetal force.
- **Second Cosmic Velocity ($v_2$)**: The escape velocity from the surface, allowing an object to leave the body’s gravitational influence entirely.
- **Third Cosmic Velocity ($v_3$)**: The speed needed to escape the star system (e.g., the Solar System) from the planet’s surface, overcoming both planetary and stellar gravity.

### 2. Mathematical Derivations

#### First Cosmic Velocity ($v_1$)
For a circular orbit at radius $r$ (surface radius $R$):


$$F_g = F_c$$


$$\frac{G M m}{r^2} = \frac{m v_1^2}{r}$$


Cancel $m$, set $r = R$:


$$v_1 = \sqrt{\frac{G M}{R}}$$


where $G$ is the gravitational constant, $M$ is the body’s mass, and $R$ is its radius.

#### Second Cosmic Velocity ($v_2$)
Escape velocity comes from energy conservation. Total mechanical energy at launch equals zero at infinity:

$$\frac{1}{2} m v_2^2 - \frac{G M m}{R} = 0$$


$$v_2 = \sqrt{\frac{2 G M}{R}}$$


Note: $v_2 = \sqrt{2} v_1 \approx 1.414 v_1$.

#### Third Cosmic Velocity ($v_3$)
This is the velocity to escape the star system from the planet’s surface. It combines escaping the planet and then the star (e.g., Sun) from the planet’s orbit. Total energy must reach zero at infinity relative to the Sun:


$$\frac{1}{2} v_3^2 - \frac{G M}{R} - \frac{G M_{\text{Sun}}}{d} = 0$$


where $d$ is the distance from the Sun, and $M_{\text{Sun}}$ is the Sun’s mass. Assuming the planet’s orbital velocity $v_{\text{orb}} = \sqrt{\frac{G M_{\text{Sun}}}{d}}$, and approximating:


$$v_3 \approx \sqrt{v_2^2 + v_{\text{esc,Sun}}^2}$$


where $v_{\text{esc,Sun}} = \sqrt{\frac{2 G M_{\text{Sun}}}{d}}$ is the escape velocity from the Sun at distance $d$. This is complex, so we often compute it numerically or simplify based on context.

#### Parameters
- **Mass ($M$)**: Higher mass increases all velocities.
- **Radius ($R$)**: Larger radius decreases velocities.
- **Distance from Star ($d$)**: Affects $v_3$, decreasing as $d$ increases.

### 3. Calculations for Celestial Bodies

#### Data
- **Earth**: $M = 5.972 \times 10^{24} \, \text{kg}$, $R = 6.371 \times 10^6 \, \text{m}$, $d = 1.496 \times 10^{11} \, \text{m}$

- **Mars**: $M = 6.417 \times 10^{23} \, \text{kg}$, $R = 3.389 \times 10^6 \, \text{m}$, $d = 2.279 \times 10^{11} \, \text{m}$

- **Jupiter**: $M = 1.898 \times 10^{27} \, \text{kg}$, $R = 6.991 \times 10^7 \, \text{m}$, $d = 7.785 \times 10^{11} \, \text{m}$

- **Sun**: $M_{\text{Sun}} = 1.989 \times 10^{30} \, \text{kg}$


#### Output (Approximate)
- **Earth**: $v_1 \approx 7.91 \, \text{km/s}$, $v_2 \approx 11.19 \, \text{km/s}$, $v_3 \approx 12.36 \, \text{km/s}$

- **Mars**: $v_1 \approx 3.55 \, \text{km/s}$, $v_2 \approx 5.03 \, \text{km/s}$, $v_3 \approx 5.64 \, \text{km/s}$

- **Jupiter**: $v_1 \approx 42.14 \, \text{km/s}$, $v_2 \approx 59.54 \, \text{km/s}$, $v_3 \approx 60.17 \, \text{km/s}$



