import time
import random
import sortari

tests=[]

t=int(input("T = "))
for i in range(0,t):
    n=int(float(input("N = ")))
    mx=int(float(input("Max = ")))
    tests.append((n,mx))

for test in tests:
    arr=[]
    arr_de_sortat=[]
    for i in range(0,int(test[0])):
        arr.append(random.randint(0,test[1]))
        arr_de_sortat.append(arr[i])
    print(f"Pentru  N = {test[0]} Max = {test[1]}")
    #Quick Sort
    start=time.time()
    try:
        sortari.quickSort(arr_de_sortat, 0, len(arr) - 1)
    except RecursionError:
        print(f"Nu se poate sorta. Fie lista este deja sortata, fie s-au apelat prea multe apeluri recursive "
              f"(Quick sort)")
    else:
        print(f"Timp quick sort: {time.time() - start}")


    arr_de_sortat=[]
    for i in range(0, int(test[0])): #folosim aceleasi numere
        arr_de_sortat.append(arr[i])

    # Merge sort
    start=time.time()
    sortari.mergeSort(arr_de_sortat)
    print(f"Timp merge sort: {(time.time()-start)}")

    #Radix sort
    start=time.time()
    sortari.radix_sort(arr_de_sortat) #Nu reconstruim lista intrucat merge sort nu este in-place
    print(f"Timp radix sort: {time.time() - start}")


    #Shell sort
    arr_de_sortat=[]
    for i in range(0, int(test[0])):
        arr_de_sortat.append(arr[i])
    start=time.time()
    sortari.shellSort(arr_de_sortat)
    print(f"Timp shell sort: {time.time() - start}")

    #Heap sort
    start=time.time()
    sortari.heapSort(arr) #ultima sortare, deci putem folosi lista initiala
    print(f"Timp heap sort: {time.time() - start}")
    print("\n")


