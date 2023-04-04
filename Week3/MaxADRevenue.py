# Programming Assignment 3:Maximum Advertisement Revenue

n = int(input()) 
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]
x.sort()
y.sort()
MaxADR = sum([x[i]*y[i] for i in range(n)])
print(MaxADR)