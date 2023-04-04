# Programming Assignment 3: Greedy Algorithms, Money Change
def change(n):
    ten = n//10
    n%=10
    five = n//5
    n%=5
    return ten+five+n

if __name__ == '__main__':
    n = int(input())
    print(change(n))
