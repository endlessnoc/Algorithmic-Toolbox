#Programming Assignment 2: Algorithmic Warm-up, Last Digit of a Large Fibonacci Number
def last_digit(a):
    a,x,y = a%60, 0 ,1
    if a==0:
        return 0
    if a==1:
        return 1
    for i in range(2,a+1):
        z = (x+y)%10
        x,y = y,z
    return z

if __name__ == '__main__':
    a = int(input())
    print(last_digit(a))
