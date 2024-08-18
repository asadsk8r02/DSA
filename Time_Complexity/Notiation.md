# Big O Notation (O)

Big O notation describes the upper bound of an algorithm's runtime or complexity. It gives the worst-case scenario of how an algorithm's performance scales with the size of the input. For example, if an algorithm has a time complexity of O(n^2), it means that in the worst case, the time taken by the algorithm grows proportionally to the square of the input size.

# Omega Notation (Ω)

Omega notation represents the lower bound of an algorithm's runtime. It gives the best-case scenario or the minimum time an algorithm will take, regardless of the input. If an algorithm has a time complexity of Ω(n)/Omega(n), it means that in the best case, the time taken by the algorithm will grow at least linearly with the input size.

# Theta Notation (Θ)

Theta notation provides a tight bound on the algorithm's runtime, meaning it describes both the upper and lower bounds. If an algorithm has a time complexity of Θ(n)/Theta(n), it means that the time taken by the algorithm grows linearly with the input size, both in the best and worst cases. In other words, Theta notation implies that the algorithm's runtime is both O(n) and Ω(n)/Omega(n).


# Theta (Θ) vs. Big O (O) and Omega (Ω):

* Theta provides a tight bound, meaning it describes the exact growth rate of an algorithm, not just the upper or lower bound.
* If an algorithm's runtime is described by Theta, it means both Big O and Omega bounds are equal, so the algorithm’s runtime will always fall within this bound.
* Big O gives you the upper bound (worst-case).
* Omega gives you the lower bound (best-case).
* Theta gives you the exact bound (tight bound) when both the upper and lower bounds are the same.

# Master Theorem Overview
The Master Theorem is a tool used to analyze the time complexity of divide-and-conquer algorithms, which are algorithms that solve a problem by recursively breaking it down into smaller subproblems of the same type. It provides a straightforward way to determine the time complexity of recurrences that fit a specific form.

## Form of Recurrence for the Master Theorem
The Master Theorem applies to recurrences of the following form:

<img width="489" alt="image" src="https://github.com/user-attachments/assets/a3c40747-f7d2-4455-abca-8a2683c6da16">

Here:
* T(n): The total time complexity for a problem of size nnn.
* a: The number of subproblems generated in each step.
* n/b: The size of each subproblem (where b>1).
* O(n^d): The time complexity of the work done outside the recursive calls, i.e., the cost of dividing the problem and combining the results.

## Cases of the Master Theorem
The Master Theorem provides three distinct cases based on the relationship between aaa, bbb, and ddd, which determine the overall time complexity T(n)T(n)T(n):

### Case 1: a > b<sup>d</sup>

Condition: log<sub>b</sub>(a) > d

Time Complexity: T(n) = O(n <sup>log<sub>b</sub>(a)</sup>)

Explanation: The recursive part (i.e., the subproblems) dominates the overall time complexity. The number of subproblems grows faster than the cost of the work done outside the recursive calls.

### Case 2: a = b<sup>d</sup>

Condition: log<sub>b</sub>(a) = d

Time Complexity: T(n) = O(n<sup>d</sup>log(n))

Explanation: The recursive part and the work done outside the recursive calls contribute equally to the time complexity. The logarithmic factor arises due to the height of the recursion tree.

### Case 3: a < b<sup>d</sup>

Condition: log<sub>b</sub>(a) < d

Time Complexity: T(n) = O(n<sup>d</sup>)

Explanation: The work done outside the recursive calls dominates the overall time complexity. The cost of dividing and combining the subproblems outweighs the recursive costs.


# Recursion Tree Method
The Recursion Tree Method is a visual and intuitive approach to analyzing the time complexity of recursive algorithms. It helps you understand how the total work of a recursive algorithm is distributed across the different levels of recursion. The method involves constructing a tree where each node represents a recursive call, and the edges represent the progression from one call to the next.

## Steps to Apply the Recursion Tree Method
### 1. Write the Recurrence Relation:

* Start by writing the recurrence relation that represents the time complexity of the recursive algorithm.

* Example: For a problem of size n, if the algorithm divides the problem into a subproblems of size n/b and does O(n<sup>d</sup>) work outside the recursive calls, the recurrence relation is:

<img width="489" alt="image" src="https://github.com/user-attachments/assets/a3c40747-f7d2-4455-abca-8a2683c6da16">

### 2. Construct the Recursion Tree:

* Draw the root of the tree to represent the original problem of size n. The work done at this level is O(n<sup>d</sup>).
* From the root, draw a branches to represent the a recursive subproblems of size n/b. Each of these subproblems will have its own subtree.
* Repeat this process recursively for each subproblem until you reach the base case (typically when the problem size becomes 1 or a constant).

### 3. Calculate the Work at Each Level:

* For each level of the tree, calculate the total amount of work done by summing the work across all nodes at that level.
* The work at the i-th level of the tree is typically the number of nodes at that level multiplied by the cost of work at each node.
* For example, if there are a<sup>i</sup> nodes at level i and each node at that level does O((n/b<sup>i</sup>)<sup>d</sup>) work, the total work at level i is:

<img width="664" alt="image" src="https://github.com/user-attachments/assets/139ebd91-b34d-499d-a919-df11cdf3b5dc">

### 4. Sum the Work Across All Levels:

* Sum the work across all levels of the tree to get the total time complexity T(n).
* If the tree has log<sub>b</sub> n levels, you sum the work done at each level from i = 0 to i = log<sub>b</sub> n.
* The total time complexity is the sum of work done at all levels:

<img width="353" alt="image" src="https://github.com/user-attachments/assets/b8a2e55b-8405-4da7-811e-37b256a07aef">

### 5. Simplify the Sum:

* After summing the work done at each level, simplify the expression to obtain the final time complexity.

## Example: Analyzing Merge Sort Using Recursion Tree Method

Recurrence Relation:

T(n) = 2T(n/2) + O(n)

### 1. Construct the Recursion Tree:
At the root (level 0), we have T(n) = O(n).
The root has 2 children, each representing a subproblem of size n/2, and each child does T(n/2) = O(n/2) work.
This process continues until the base case is reached.

### 2. Calculate Work at Each Level:
* Level 0: 1 node, work = O(n)
* Level 1: 2 nodes, work = 2 × O(n/2) = O(n)
* Level 2: 4 nodes, work = 4 × O(n/4) = O(n)
…
* Level i: 2<sup>i</sup> nodes, work = 2<sup>i</sup> × O(n/2<sup>i</sup>) = O(n)

### 3.Sum the Work Across All Levels:
* Since each level does O(n) work and there are log<sub>2</sub> n levels:

T(n) = O(n) + O(n) + … + O(n) (log n terms)

* Total work = O(n log n).

## Key Points to Remember
* Balanced Recursion Trees: When the recursive algorithm divides the problem into equal-sized subproblems (like merge sort), the recursion tree is balanced, making it easier to sum the work across levels.
* Unbalanced Recursion Trees: For algorithms like quicksort, where the partition might not always be balanced, the recursion tree can be skewed. The method still applies but requires careful attention to the varying size of subproblems.
* Base Cases: The height of the tree is typically log<sub>b</sub> n, where b is the factor by which the problem size decreases in each recursive step. The work done at the base case level is usually a constant.












