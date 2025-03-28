# Problem 1
Let’s tackle the **Option 2: Advanced Task – Full Implementation** for calculating the equivalent resistance of a circuit using graph theory. We’ll implement the algorithm in Python, using the `networkx` library for graph manipulation, and test it on three example circuits: simple series, simple parallel, and a nested configuration. The solution will include a detailed explanation, implementation, test cases, and an analysis of efficiency.

[Simulation](Problem_1.py)


---

## Equivalent Resistance Using Graph Theory

### Motivation
Calculating equivalent resistance is crucial in electrical circuit design, but traditional methods (series and parallel rules) can be cumbersome for complex circuits. Graph theory provides a systematic approach by representing circuits as graphs—nodes as junctions and edges as resistors with weights (resistance values). This method simplifies complex networks, enables automation, and connects electrical engineering with mathematical concepts, benefiting applications like circuit simulation and network optimization.

---

### Algorithm Description
The algorithm iteratively simplifies the graph by identifying and reducing series and parallel resistor configurations until a single equivalent resistance remains. Here’s the high-level approach:

1. **Graph Representation**:
   - Nodes represent junctions in the circuit.
   - Edges represent resistors, with weights as resistance values.
   - Input: A graph with two terminal nodes (start and end) between which we calculate the equivalent resistance.

2. **Iterative Simplification**:
   - **Series Reduction**: Identify nodes with degree 2 (exactly two neighbors). If a node $v$ connects nodes $u$ and $w$ with resistors $R_1$ (between $u$ and $v$) and $R_2$ (between $v$ and $w$), replace with a single edge between $u$ and $w$ with resistance $R_1 + R_2$, and remove $v$.
   - **Parallel Reduction**: Identify pairs of nodes connected by multiple edges (parallel resistors). For edges between nodes $u$ and $v$ with resistances $R_1, R_2, \ldots, R_n$, replace with a single edge with resistance $\frac{1}{\frac{1}{R_1} + \frac{1}{R_2} + \cdots + \frac{1}{R_n}}$.
   - Repeat until the graph reduces to a single edge between the start and end nodes.

3. **Handling Nested Configurations**:
   - Use a traversal (e.g., DFS) to explore the graph and identify series/parallel patterns.
   - For nested configurations, the iterative process naturally handles them by reducing inner series/parallel subgraphs first, working outward.

---

### Implementation in Python

We’ll use the `networkx` library to represent and manipulate the graph. The implementation will:
- Accept a graph with resistors as weighted edges.
- Iteratively simplify the graph.
- Output the equivalent resistance.


### Explanation of the Algorithm and Implementation

#### How It Works
1. **Graph Representation**:
   - We use `networkx.MultiGraph` to allow multiple edges between nodes (for parallel resistors).
   - Each edge has a `resistance` attribute (e.g., `G.add_edge(0, 1, resistance=2)`).

2. **Series Reduction**:
   - Identify nodes with degree 2 (excluding start and end nodes).
   - For a node $v$ with neighbors $u$ and $w$, combine resistances $R_1 + R_2$, add a new edge $(u, w)$, and remove $v$.

3. **Parallel Reduction**:
   - Identify pairs of nodes with multiple edges.
   - Compute the equivalent resistance using the parallel formula $\frac{1}{R_{eq}} = \sum \frac{1}{R_i}$, replace with a single edge, and remove the old edges.

4. **Iteration**:
   - Alternate between series and parallel reductions until the graph reduces to a single edge between the start and end nodes.

#### Handling Nested Configurations
- The algorithm naturally handles nested configurations by reducing inner patterns first:
  - In Test 3, it first reduces the parallel pair $(2\Omega || 2\Omega) = 1\Omega$ between nodes 0 and 1, and $(4\Omega || 4\Omega) = 2\Omega$ between nodes 1 and 2.
  - Then, it performs a series reduction on the resulting $1\Omega + 2\Omega = 3\Omega$.

---

### Test Cases and Results

#### Test 1: Simple Series
- **Graph**: $0 \xrightarrow{2\Omega} 1 \xrightarrow{3\Omega} 2$
- **Expected**: $2 + 3 = 5 \, \Omega$
- **Calculated**: $5 \, \Omega$

#### Test 2: Simple Parallel
- **Graph**: Two edges between nodes 0 and 1, each $2 \, \Omega$
- **Expected**: $\frac{1}{\frac{1}{2} + \frac{1}{2}} = 1 \, \Omega$
- **Calculated**: $1 \, \Omega$

#### Test 3: Nested Configuration
- **Graph**: $(2\Omega || 2\Omega)$ in series with $(4\Omega || 4\Omega)$
- **Expected**:
  - First parallel: $2 || 2 = 1 \, \Omega$
  - Second parallel: $4 || 4 = 2 \, \Omega$
  - Series: $1 + 2 = 3 \, \Omega$
- **Calculated**: $3 \, \Omega$

---

### Efficiency Analysis and Potential Improvements

#### Efficiency
- **Time Complexity**:
  - Series reduction: $O(|V|)$ per iteration to find a degree-2 node.
  - Parallel reduction: $O(|E|)$ to find multi-edges.
  - Number of iterations: In the worst case, each iteration removes one node or edge, so up to $O(|V| + |E|)$ iterations.
  - Total: $O((|V| + |E|) \cdot (|V| + |E|))$, roughly $O(|V|^2 + |E|^2)$.
- **Space Complexity**: $O(|V| + |E|)$ for storing the graph.

#### Limitations
- The current implementation assumes the circuit can be reduced using only series and parallel rules, which fails for complex graphs with cycles (e.g., bridge circuits like the Wheatstone bridge).
- It doesn’t handle delta-star transformations, which are needed for non-series-parallel graphs.

#### Improvements
1. **Delta-Star Transformation**:
   - Add a step to detect delta configurations (three nodes forming a triangle) and convert them to star configurations, allowing further series/parallel reductions.
2. **Matrix Methods**:
   - Use the Laplacian matrix and Kirchhoff’s laws to compute equivalent resistance directly, which handles arbitrary graphs but is more computationally intensive ($O(|V|^3)$ for matrix inversion).
3. **Optimization**:
   - Use a priority queue to identify reducible patterns more efficiently.
   - Implement cycle detection to handle complex graphs with non-series-parallel structures.

---

### Deliverables Summary
- **Implementation**: Provided in Python using `networkx`.
- **Test Cases**: Three examples (series, parallel, nested) with expected and calculated results.
- **Analysis**: Discussed efficiency and suggested improvements like delta-star transformations.

This solution demonstrates how graph theory simplifies equivalent resistance calculations, with potential for extension to more complex circuits. Let me know if you’d like to explore additional test cases or improvements!
