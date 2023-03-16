import time
import random
import sortari

arr_quick=[]
arr_merge=[]
for i in range(0,10000):
    arr_quick.append(random.randint(0,1000000))
    arr_merge.append(arr_quick[i])
print(arr_quick)
start=time.time()
sortari.quickSort(arr_quick,0,len(arr_quick)-1)
print(arr_quick)
print(f"Timp quick sort: {time.time() - start}")
start=time.time()
sortari.mergeSort(arr_merge)
print(arr_merge)
print(f"Timp merge sort:{(time.time()-start)}")