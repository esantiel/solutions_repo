import java.util.ArrayList;

public class LorentzForceSimulation {
    // Particle properties
    static double q = 1.6e-19;  // Charge (Coulombs, e.g., electron charge)
    static double m = 9.11e-31; // Mass (kg, e.g., electron mass)
    static double dt = 1e-9;    // Time step (seconds)
    static int steps = 1000;    // Number of simulation steps

    // Vector class to represent 3D vectors
    static class Vector3D {
        double x, y, z;

        Vector3D(double x, double y, double z) {
            this.x = x;
            this.y = y;
            this.z = z;
        }

        // Vector addition
        Vector3D add(Vector3D v) {
            return new Vector3D(x + v.x, y + v.y, z + v.z);
        }

        // Scalar multiplication
        Vector3D scale(double s) {
            return new Vector3D(x * s, y * s, z * s);
        }

        // Cross product
        Vector3D cross(Vector3D v) {
            return new Vector3D(
                y * v.z - z * v.y,
                z * v.x - x * v.z,
                x * v.y - y * v.x
            );
        }
    }

    // Lorentz force calculation: F = q(E + v x B)
    static Vector3D lorentzForce(Vector3D v, Vector3D E, Vector3D B) {
        Vector3D vCrossB = v.cross(B);
        return E.add(vCrossB).scale(q);
    }

    // RK4 step for velocity and position
    static class State {
        Vector3D r, v;

        State(Vector3D r, Vector3D v) {
            this.r = r;
            this.v = v;
        }
    }

    static State rk4Step(State state, Vector3D E, Vector3D B, double dt) {
        Vector3D r = state.r;
        Vector3D v = state.v;

        // k1
        Vector3D k1_v = lorentzForce(v, E, B).scale(1.0 / m);
        Vector3D k1_r = v;

        // k2
        Vector3D v2 = v.add(k1_v.scale(dt / 2));
        Vector3D k2_v = lorentzForce(v2, E, B).scale(1.0 / m);
        Vector3D k2_r = v2;

        // k3
        Vector3D v3 = v.add(k2_v.scale(dt / 2));
        Vector3D k3_v = lorentzForce(v3, E, B).scale(1.0 / m);
        Vector3D k3_r = v3;

        // k4
        Vector3D v4 = v.add(k3_v.scale(dt));
        Vector3D k4_v = lorentzForce(v4, E, B).scale(1.0 / m);
        Vector3D k4_r = v4;

        // Update position and velocity
        Vector3D r_new = r.add(k1_r.add(k2_r.scale(2)).add(k3_r.scale(2)).add(k4_r).scale(dt / 6));
        Vector3D v_new = v.add(k1_v.add(k2_v.scale(2)).add(k3_v.scale(2)).add(k4_v).scale(dt / 6));

        return new State(r_new, v_new);
    }

    // Simulation function
    static void simulate(String scenario) {
        // Initial conditions
        Vector3D r0 = new Vector3D(0, 0, 0);           // Initial position
        Vector3D v0 = new Vector3D(1e5, 0, 0);         // Initial velocity (m/s)
        Vector3D E, B;

        // Field configurations
        switch (scenario) {
            case "uniformB":
                E = new Vector3D(0, 0, 0);             // No electric field
                B = new Vector3D(0, 0, 1);             // Uniform B along z (1 Tesla)
                break;
            case "combinedEB":
                E = new Vector3D(1e5, 0, 0);           // E along x (V/m)
                B = new Vector3D(0, 0, 1);             // B along z
                break;
            case "crossedEB":
                E = new Vector3D(0, 1e5, 0);           // E along y
                B = new Vector3D(0, 0, 1);             // B along z
                break;
            default:
                System.out.println("Invalid scenario");
                return;
        }

        // Store trajectory
        ArrayList<Vector3D> trajectory = new ArrayList<>();
        State state = new State(r0, v0);
        trajectory.add(state.r);

        // Run simulation
        for (int i = 0; i < steps; i++) {
            state = rk4Step(state, E, B, dt);
            trajectory.add(state.r);
        }

        // Output trajectory (x, y, z coordinates)
        System.out.println("Trajectory for " + scenario + ":");
        for (int i = 0; i < trajectory.size(); i += 50) { // Sample every 50 steps for brevity
            Vector3D pos = trajectory.get(i);
            System.out.printf("Step %d: (%.2e, %.2e, %.2e)\n", i, pos.x, pos.y, pos.z);
        }
    }

    public static void main(String[] args) {
        // Run simulations for all three scenarios
        System.out.println("Simulation 1: Uniform Magnetic Field");
        simulate("uniformB");

        System.out.println("\nSimulation 2: Combined Electric and Magnetic Fields");
        simulate("combinedEB");

        System.out.println("\nSimulation 3: Crossed Electric and Magnetic Fields");
        simulate("crossedEB");
    }
}