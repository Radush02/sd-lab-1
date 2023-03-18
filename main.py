import time
import random
import sortari

arr=[] #pt merge & radix
arr_quick=[]
for i in range(0,int(1e4)):
    arr.append(random.randint(0,1000000))
    arr_quick.append(arr[i])

start=time.time()
sortari.mergeSort(arr)
#print(*sortari.mergeSort(arr))
print(f"Timp merge sort: {(time.time()-start)}")

start=time.time()
try:
    sortari.quickSort(arr_quick, 0, len(arr) - 1)
except RecursionError:
    print("Lista este deja sortata (Quick sort).")
else:
    print(f"Timp quick sort: {time.time() - start}")

start=time.time()
sortari.radix_sort(arr)
print(f"Timp radix sort: {time.time() - start}")



