### PARAMETERS ###
param n;
param costBound;
param value {i in 0..n-1} >= 0;
param cost {i in 0..n-1} >= 0;

### VARIABLES ###
var object{i in 0..n-1} binary;
var totalCost = sum{i in 0..n-1} object[i] * cost[i];
var totalVal = sum{i in 0..n-1} object[i] * value[i];


### OBJECTIVE ###
maximize totalValue: sum{i in 0..n-1} object[i] * value[i];

### CONSTRAINTS ###
subject to constraint1: sum{i in 0..n-1} object[i] * cost[i] <= costBound;

