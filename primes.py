import math
import numpy as np 
def primes(n=100,show=True):
    primes=np.array([])
    numbers=np.arange(2,n)
    while numbers.size>0:
        primes=np.append(primes,numbers[0])
        numbers=np.array([x for x in numbers if x%primes[-1]!=0])
    if show==True:
        [print(int(x),end=', ') for x in primes]
    return primes, len(primes)

print(primes(10000,show=False)[1])