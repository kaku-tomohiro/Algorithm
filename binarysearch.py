n = int(input())
s = list(map(int, input().split()))
q = int(input())
t = list(map(int, input().split()))

count = 0
for item in t:
    middle = int((n - 1) / 2)
    upper = n - 1
    lower = 0
    while(True):
        if s[middle] == item:
            count += 1
            break
        elif lower >= upper:
            break
        elif s[middle] > item:
            upper = middle
            middle = int((lower + lower) / 2)
        elif s[middle] < item:
            lower = middle + 1
            middle = int((upper + lower) / 2)

print(count)



