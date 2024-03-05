## 70. Climbing Stairs

### Problem Statement:

You are climbing a staircase. It takes n steps to reach the top. 
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

### Solution:

If we imagine a set of stairs and work from the top of the stairs downward, we can break the problem into sub-problems. 
From the top step, we know that there is only one way to land there. From the second step from the top, we are only able to take one step towards the top of the stairs as two steps would make us overshoot. 

Working downwards now, we can see that the number of solutions to reach the top of the stairs from some step N in total number of stairs X is the sum of solutions from the (X-N) stairs above N. 