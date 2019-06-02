### SETS ###
set edgeList dimen 2;


### PARAMETERS ###
# number of nodes
param numNodes;

# number of colors
param numColors;

# edge[op1, op2] = 1 iff (i,j) is in edgeList
param edge {i in 0..numNodes-1, j in 0..numNodes-1} :=
(if (i,j) in edgeList or (j,i) in edgeList then 1 else 0);


### VARIABLES ###
#color[i,c] = 1 means that node i is assigned color c
var color {i in 0..numNodes-1, c in 0..numColors-1} binary;

#conflict[i,j] = 1 means that there is a conflict in the
# coloring of nodes i and j
var conflict {i in 0..numNodes-1, j in 0..numNodes-1} binary;


### OBJECTIVE ###
minimize numConflicts: sum {i in 0..numNodes-1, j in 0..numNodes-1} conflict[i,j];


### CONSTRAINTS ###
# each node has exactly one color
subject to constraint1 {i in 0..numNodes-1}:
	sum {c in 0..numColors-1} color[i,c] = 1;

# detect conflicts
constraint2 {i in 0..numNodes-1, j in 0..numNodes-1, c in 0..numColors-1}:
	edge[i,j] * (color[i,c] + color[j,c] - 1) - conflict[i,j] <= 0;

