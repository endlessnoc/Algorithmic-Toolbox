#Programming Assignment 2: Algorithmic Warm-up, Fibonacci Number

x = [0,1]
def FN(abc):
    if abc==0:
        return 0
    if abc==1:
        return 1
    for i in range(2,abc+1):
        x.append(x[i-1]+x[i-2])
    return x[-1]

abc = int(input())
print(FN(abc))
