# results

# Usage
To run knapsack or coloring algorithms on all inputs with a time limit per problem, simply change to the respective directory, and run `python3 coloring.py <timelimit>` or `python3 knapsack.py <timelimit>`. The timelimit parameter is in seconds.

# Knapsack
The Knapsack solution provided aims to optimize an array of binary variables which represent whether each object has been selected. This optimization is subject to the constraint that the total cost of all selected items must be less than or equal to the cost bound. CPLEX is able to solve all given instances of this in well under the time limit. The solutions found are all at least as good as those found by greedy and exhaustive algorithms.

# Coloring
