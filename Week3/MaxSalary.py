#Programming Assignment 3: Greedy Algorithms, Maximum Salary (Largest Number)

#先輸入有幾個數字(Enter)
#再分別輸入數字，以空白隔開

numbers = int(input()) ; EnterN = [int(i) for i in input().split()]
#d = Digit
def F1(d, maxd):
    return int(str(d)+str(maxd))  >=  int(str(maxd)+str(d))
def F2(first):
    ans = []
    while first != []:
        maxd = 0
        for d in first:
            if F1(d, maxd):
                maxd = d
        ans.append(maxd)
        first.remove(maxd)
    return ans

print("".join([str(i) for i in F2(EnterN)]))