# Problem 1


# Orbital Period and Orbital Radius




# Project Documentation


<iframe width="560" height="315" src="https://www.youtube.com/embed/bcvnfQlz1x4?si=bl428S7Xqp5I51gK" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


## Task Breakdown

<span style="font-family: Arial; font-size: 20px;">[Simulation](Problem_1.html)</span>

### 1. Derivation of the Relationship

For a circular orbit, the gravitational force provides the centripetal force required to keep an object (mass $m$) orbiting a central body (mass $M$) at radius $r$.

#### Gravitational Force
$$F_g = \frac{G M m}{r^2}$$

where $G$ is the gravitational constant ($6.67430 \times 10^{-11} \, \text{m}^3 \text{kg}^{-1} \text{s}^{-2}$).


#### Centripetal Force
For circular motion with orbital speed $v$ and period $T$:

$$v = \frac{2\pi r}{T}$$

Centripetal force:

$$F_c = \frac{m v^2}{r} = \frac{m}{r} \left( \frac{2\pi r}{T} \right)^2 = \frac{4\pi^2 m r}{T^2}$$

![alt text](centripetalforce0.gif)

#### Equate Forces
$$\frac{G M m}{r^2} = \frac{4\pi^2 m r}{T^2}$$

Cancel $m$ (assuming $m \neq 0$):

$$\frac{G M}{r^2} = \frac{4\pi^2 r}{T^2}$$

Rearrange:

$$T^2 = \frac{4\pi^2}{G M} r^3$$

Thus:

$$T^2 = k r^3$$

where $k = \frac{4\pi^2}{G M}$ is a constant for a given central mass $M$. This is Kepler’s Third Law for circular orbits.


---


### 2. Implications for Astronomy

- **Mass Determination**: If $T$ and $r$ are measured (e.g., via observation), $M$ can be calculated:

$$M = \frac{4\pi^2 r^3}{G T^2}$$

  This is how we estimate the Sun’s mass using Earth’s orbit or Earth’s mass using the Moon’s orbit.

- **Distance Calculation**: Knowing $T$ and $M$, solve for $r$:

$$r = \left( \frac{G M T^2}{4\pi^2} \right)^{1/3}$$

- **System Scaling**: For planets orbiting the Sun, $T^2 / r^3$ is constant, allowing comparisons across the Solar System.

---

### 3. Real-World Examples

#### Moon’s Orbit Around Earth
- $r \approx 384,400 \, \text{km} = 3.844 \times 10^8 \, \text{m}$

- $T \approx 27.32 \, \text{days} = 2.360 \times 10^6 \, \text{s}$

- $M_{\text{Earth}} \approx 5.972 \times 10^{24} \, \text{kg}$

Check:

$$T^2 = (2.360 \times 10^6)^2 = 5.570 \times 10^{12} \, \text{s}^2$$

$$r^3 = (3.844 \times 10^8)^3 = 5.677 \times 10^{25} \, \text{m}^3$$

$$k = \frac{T^2}{r^3} = \frac{5.570 \times 10^{12}}{5.677 \times 10^{25}} \approx 9.81 \times 10^{-14} \, \text{s}^2 \text{m}^{-3}$$

$$M = \frac{4\pi^2}{G k} = \frac{4\pi^2}{6.67430 \times 10^{-11} \cdot 9.81 \times 10^{-14}} \approx 6.02 \times 10^{24} \, \text{kg}$$

Close to Earth’s actual mass, confirming the law.

#### Earth’s Orbit Around Sun
- $r \approx 1 \, \text{AU} = 1.496 \times 10^{11} \, \text{m}$

- $T \approx 1 \, \text{year} = 3.156 \times 10^7 \, \text{s}$

- $M_{\text{Sun}} \approx 1.989 \times 10^{30} \, \text{kg}$

Verify similarly; the constant matches the Sun’s mass.

---

## Deliverables

### Explanation
- **Derivation**: $T^2 = \frac{4\pi^2}{G M} r^3$ links period and radius via gravity and centripetal motion.
- **Implications**: Enables mass and distance calculations, foundational for astronomy.
- **Examples**: Moon, Earth, and Mars orbits align with the law, verifiable computationally.

### Graphical Representations
- **T² vs r³ Plot**: Log-log scale shows linearity, with real bodies overlaid.
- **Circular Orbits**: Visualizes paths, scaled to show relative sizes.

### Extension to Elliptical Orbits
Kepler’s Third Law generalizes to elliptical orbits using the semi-major axis $a$ instead of $r$:

$$T^2 = \frac{4\pi^2}{G M} a^3$$

For circular orbits, $a = r$, so the form holds. This applies to comets, exoplanets, and binary stars, with $M$ as the total mass of the system.

---

## Discussion
The $T^2 \propto r^3$ relationship is a triumph of classical physics, bridging Kepler’s empirical discovery with Newton’s mechanics. It assumes circular orbits and a dominant central mass, but extends robustly to elliptical cases. Limitations include neglecting relativistic effects (e.g., Mercury’s precession) or multi-body interactions, which require perturbations or numerical methods.

The simulation confirms the law across scales—from the Moon to Mars—making it a powerful tool for education and exploration.
