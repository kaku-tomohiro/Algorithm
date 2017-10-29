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


n = int(input())
A = list(map(int, input().split()))

SelectionSort(A)
SelectionSort([1,2,3,4,5])

def selectionSort(a):
    count = 0
    for i in range(len(a)):
        mini = i
        for j in range(i,len(a)):
            if a[j] < a[mini]:
                mini = j
        if i != mini:
            ret = a[i]
            a[i] = a[mini]
            a[mini] = ret
            count += 1
    print(" ".join(map(str,a)))
    print(count)
n = int(input())
a = list(map(int,input().split()))
selectionSort(a)