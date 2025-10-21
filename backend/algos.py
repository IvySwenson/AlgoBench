# backend/algos.py

def quicksort(a):
    def qs(l, r):
        if l >= r: return
        i, j = l, r
        pivot = a[(l + r)//2]
        while i <= j:
            while a[i] < pivot: i += 1
            while a[j] > pivot: j -= 1
            if i <= j:
                a[i], a[j] = a[j], a[i]
                i += 1; j -= 1
        qs(l, j)
        qs(i, r)
    if a:
        qs(0, len(a)-1)

def mergesort(a):
    if len(a) <= 1: return
    mid = len(a)//2
    L, R = a[:mid], a[mid:]
    mergesort(L); mergesort(R)
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            a[k] = L[i]; i += 1
        else:
            a[k] = R[j]; j += 1
        k += 1
    while i < len(L): a[k] = L[i]; i += 1; k += 1
    while j < len(R): a[k] = R[j]; j += 1; k += 1

def heapsort(a):
    n = len(a)
    def heapify(i, n_):
        largest = i
        l, r = 2*i+1, 2*i+2
        if l < n_ and a[l] > a[largest]: largest = l
        if r < n_ and a[r] > a[largest]: largest = r
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            heapify(largest, n_)
    for i in range(n//2 - 1, -1, -1):  # build heap
        heapify(i, n)
    for i in range(n-1, 0, -1):        # extract
        a[0], a[i] = a[i], a[0]
        heapify(0, i)

def bubblesort(a):
    n = len(a)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped: break

ALGORITHMS = {
    "QuickSort": quicksort,
    "MergeSort": mergesort,
    "HeapSort": heapsort,
    "BubbleSort": bubblesort,
}
