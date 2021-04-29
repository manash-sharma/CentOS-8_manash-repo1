#!/usr/bin/python
num=input("Enter numbers to find average:")
res=[int(x) for x in str(num)]
avg=sum(res)/len(res)
print (avg)
