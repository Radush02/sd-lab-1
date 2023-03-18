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
#Doar pentru concept. Nu va rula in programul principal.
def bogosort(arr):
    while bogo_sortat(arr)==0:
        shuffle(arr)
    return arr
def bogo_sortat(arr):
    for i in range(0,len(arr)-2):
        if arr[i]>arr[i+1]:
            return 0
    return 1