#Programming Assignment 2: Algorithmic Warm-up, Least Common Multiple
def leastcommonM(a, b):
   if a > b:
       big = a
   else:
       big = b
   while(True):
       if ((big%a == 0) and (big%b == 0)):
           lcm = big
       big += 1
       break
   return lcm

a,b = map(int, input().split())
print(leastcommonM(a, b))