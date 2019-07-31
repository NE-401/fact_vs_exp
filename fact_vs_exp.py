#!/usr/bin/env python3
import sys

def fact(n):
    a=1
    for i in range(1,n+1):
        a*=i

    return a

def exp(b,n):
    return b**n

base=5
limit=20

if len(sys.argv) == 2:
    limit=int(sys.argv[1])
elif len(sys.argv) == 3:
    limit=int(sys.argv[1])
    base=int(sys.argv[2])
elif len(sys.argv) > 3:
    print('too much argument')
    print('usage: ./fact_vs_exp.py [limit [base]]')
    exit()

print('exp base = {0}'.format(base))
print('iteration limit = {0}'.format(limit))

for i in range(1,limit+1):
    print('factorial of {0} = {1}'.format(i,fact(i)))
    print('{0}^{1}            = {2}'.format(base,i,exp(base,i)))
