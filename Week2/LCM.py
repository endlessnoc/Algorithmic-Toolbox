#Programming Assignment 2: Algorithmic Warm-up, Least Common Multiple
def greatestCommonD(a, b):
    if not b:
        return a
    return greatestCommonD(b, a % b)

def leastcommomM(a, b):
    return (a * b) // greatestCommonD(a, b)

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(leastcommomM(a, b))
