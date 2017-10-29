n = int(input())
list = []
for _ in range(n):
    command = input().split()
    if command[0] == 'insert':
        num = int(command[1])
        list.insert(0, num)
    elif command[0] == 'delete':
        num = int(command[1])
        try:
            list.remove(num)
        except:
            pass
    elif command[0] == 'deleteFirst':
        list.pop(0)
    elif command[0] == 'deleteLast':
        list.pop()

print(" ".join(map(str, list)))

from collections import deque
import sys

dq = deque()
num = int(sys.stdin.readline())
line = sys.stdin.readlines()

for i in range(num):

    order = line[i].split()

    if order[0] == 'insert':
        dq.appendleft(order[1])
    elif order[0] == 'deleteFirst':
        dq.popleft()
    elif order[0] == 'deleteLast':
        dq.pop()
    else:
        if order[1] in dq:
            dq.remove(order[1])

print(' '.join(dq))