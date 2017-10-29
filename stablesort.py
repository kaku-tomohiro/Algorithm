def bubbleSort(A, N):
    flag = 1
    count = 0
    while flag == 1:
        flag = 0
        for i in range(1, N)[::-1]:
            if A[i] < A[i - 1]:
                tmp = A[i]
                A[i] = A[i - 1]
                A[i - 1] = tmp
                flag = 1
                count += 1
    print(" ".join(map(str, A)))
    print(count)
    return A

def SelectionSort(A):
    count = 0
    for i in range(len(A)):
        minj = i
        for j in range(i, len(A)):
            if A[j] < A[minj]:
                minj = j
        if i != minj:
            A[i], A[minj] = A[minj], A[i]
            count += 1
    print(" ".join(map(str, A)))
    print(count)
    return A

n = int(input())
a = input().split()
#bubble sort always stable

#compare bubble and selection judge stabel or not