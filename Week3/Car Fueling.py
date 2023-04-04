#Programming Assignment 3: Greedy Algorithms, Car Fueling

#print("請輸入Distane，滿油箱最大行駛距離，路途中加油站數量，中間輸入完按Enter")
#print("輸入完上述後再輸入加油站的位置，中間以空格隔開")
#print("最後將顯示停留加油次數")
#例如如果總距離為1000,車子滿油可行駛500，路途中在200,400,600,800有加油站(共四個)
#則輸入1000(Enter)500(Enter)4(Enter)200 400 600 800，Output=2代表要加兩次油


d = int(input()) #distane
m = int(input()) #the car can travel at most m miles on a full tank
n = int(input()) #Number of gas sations
i = input() #距離的list
x = [0] + list(map(int, i.split())) + [d]

def CarF(x, m, n):
    cur = 0
    c = 0
    while cur <= n:
        last = cur
        while cur <= n and x[cur + 1] - x[last] <= m:
            cur = cur + 1
        if cur == last:
            return -1
        if cur <= n:
            c = c + 1
    return c

print(CarF(x, m, n))