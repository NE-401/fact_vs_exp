#!/usr/bin/env python3

def fact(n):
    a=1
    for i in range(1,n+1):
        a*=i

    return a

def exp(b,n):
    return b**n

base=5
limit=20

for i in range(1,limit+1):
    print('factorial of {0} = {1}'.format(i,fact(i)))
    print('{0}^{1}            = {2}'.format(i,base,exp(base,i)))
