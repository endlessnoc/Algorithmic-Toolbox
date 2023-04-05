#Programming Assignment 2: Algorithmic Warm-up,Last Digit of the Sum of Squares of Fibonacci Numbers

def FN(n):
    x,y = 0,1
    for _ in range(n-1):
        x,y=y,(x+y)%10
    return y

def FN2(n):
    n %= 60
    if n<=0:
        return n
    else:
        return (FN(n)*FN(n+1))%10

if __name__ == '__main__':
    n = int(input())
    print(FN2(n))