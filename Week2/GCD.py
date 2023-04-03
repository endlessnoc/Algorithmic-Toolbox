#Programming Assignment 2: Algorithmic Warm-up, Greatest Common Divisor
def highestcommonfactor(a, b):
    if(b == 0):
        return abs(a)
    else:
        return highestcommonfactor(b, a % b)
 
a,b = map(int, input().split())
 
print(highestcommonfactor(a, b))
