#Programming Assignment 2: Algorithmic Warm-up,Last Digit of the Sum of Fibonacci Numbers
def FNsum(n):
    R=n%60 ; x,y = 0,1
    for _ in range(R+1):
        x,y=y,x+y
    return (y-1) % 10
    
if __name__ == '__main__':
    n = int(input())
    print(FNsum(n))