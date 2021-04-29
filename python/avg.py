#!/usr/bin/python
from statistics import mean
num=input("Enter set of numbers to find average:")
res=[int(x) for x in str(num)]
#res=[num]
a=mean(res)
print(a)
