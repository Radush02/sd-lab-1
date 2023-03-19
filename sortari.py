from random import shuffle
def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if(arr[j]<=pivot):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def quickSort(arr,low,high):
    if low<high:
        p=partition(arr,low,high)
        quickSort(arr,low,p-1)
        quickSort(arr,p+1,high)

def mergeSort(arr):
    lg=len(arr)
    if lg<2:
        return arr
    mij=lg//2
    st=arr[:mij]
    dr=arr[mij:]
    st=mergeSort(st)
    dr=mergeSort(dr)
    return merge(st,dr)

def merge(st,dr):
    rez=[]
    i=j=0
    while i<len(st) and j<len(dr):
        if st[i]<dr[j]:
            rez.append(st[i])
            i+=1
        else:
            rez.append(dr[j])
            j+=1
    rez+=st[i:]
    rez+=dr[j:]
    return rez

def counting(arr,cif):
    cnt=[0]*10
    rez=[0]*len(arr)
    for nr in arr:
        cnt[(nr//(10**cif))%10]+=1
    for i in range(1,10):
        cnt[i]+=cnt[i-1]
    for i in range(len(arr)-1,-1,-1):
        rez[cnt[(arr[i]//(10**cif))%10]-1]=arr[i]
        cnt[(arr[i]//(10**cif))%10]-=1
    for i in range(len(arr)):
        arr[i]=rez[i]

def radix_sort(arr):
    cif_max=len(str(max(arr)))
    for i in range(0,cif_max):
        counting(arr,i)
    return arr

def shellSort(arr):
    n=len(arr)
    k=len(arr)//2
    while k>0:
        for i in range(k,n):
            aux=arr[i]
            j=i
            while j>=k and arr[j-i]>aux:
                arr[j]=arr[j-k]
                j-=k
            arr[j]=aux
        k//=2

def heapify(arr,i,n): #folosim max heap pt ordonare crescatoare
    st=2*i+1
    dr=2*i+2
    mn=i

    if st<n and arr[st] > arr[mn]: #arr[st] < arr[mn] pt minheap
        mn=st
    if dr<n and arr[dr] > arr[mn]: # ^^^
        mn=dr

    if mn!=i:
        arr[i],arr[mn]=arr[mn],arr[i]
        heapify(arr,mn,n)

def heapSort(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,i,n)
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,0,i)


#Nu vor rula in programul principal datorita complexitatii. Bogo sort(O(n+1)!), bubble sort (O(n^2))
def bogosort(arr):
    while bogo_sortat(arr)==0:
        shuffle(arr)
    return arr
def bogo_sortat(arr):
    for i in range(0,len(arr)-2):
        if arr[i]>arr[i+1]:
            return 0
    return 1

def bubble_sort(arr):
    n=len(arr)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
