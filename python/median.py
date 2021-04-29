#!/usr/bin/python
from statistics import median
num=input("Enter number to find median:")
con=[int(x) for x in str(num)]
res=median(con)
print(res)
