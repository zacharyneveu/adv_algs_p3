param n >= 0;
param costBound >= 0;
param value {i in 0..n-1} >= 0;
param cost  {i in 0..n-1} >= 0;

var Select {i in 0..n-1} binary;

maximize Z:
	sum {i in 0..n-1} Select[i] * value[i];

subject to c1:
	sum {i in 0..n-1} cost[i] * Select[i] <= costBound;
