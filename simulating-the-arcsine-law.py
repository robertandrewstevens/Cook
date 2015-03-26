# http://www.johndcook.com/blog/2015/02/17/simulating-the-arcsine-law/

import random
from numpy import arcsin, pi, sqrt
 
def step():
    u = random.random()
    return 1 if u < 0.5 else -1
 
M = 1000 # outer loop    
N = 1000 # inner loop
 
x = 0.3 # Use any 0 < x < 1 you'd like.
 
outer_count = 0
for _ in range(M):
    n = 0
    position= 0 
    inner_count = 0
    for __ in range(N):
        position += step()
        if position > 0:
            inner_count += 1
    if inner_count/N < x:
        outer_count += 1
 
print (outer_count/M)
print (2*arcsin(sqrt(x))/pi)
