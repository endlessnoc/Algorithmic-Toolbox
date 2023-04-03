#Programming Assignment 1: Sum of Two Digits
def sum(x, y):
    return x + y

if __name__ == '__main__':
    x, y = map(int, input().split())
    print(sum(x, y))
