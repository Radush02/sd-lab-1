import time
import random
import sortari
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline,BSpline

tests=[]
rez=[[],[],[],[],[]]
f=open("teste.txt",'r')
t=int(f.readline().strip().split()[0])
for i in range(0,t):
    k=f.readline().strip().split()
    print(k)
    tests.append((int(float(k[0])),int(float(k[1]))))

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
        try:
            rez[0].append(rez[0][len(rez[0])-1])
        except:
            rez[0].append(0)
    else:
        timp=time.time() - start
        rez[0].append(timp)
        print(f"Timp quick sort: {timp}")


    arr_de_sortat=[]
    for i in range(0, int(test[0])): #folosim aceleasi numere
        arr_de_sortat.append(arr[i])

    # Merge sort
    start=time.time()
    sortari.mergeSort(arr_de_sortat)
    timp=time.time()-start
    rez[1].append(timp)
    print(f"Timp merge sort: {timp}")

    #Radix sort
    start=time.time()
    sortari.radix_sort(arr_de_sortat) #Nu reconstruim lista intrucat merge sort nu este in-place
    timp=time.time() - start
    rez[2].append(timp)
    print(f"Timp radix sort: {timp}")


    #Shell sort
    arr_de_sortat=[]
    for i in range(0, int(test[0])):
        arr_de_sortat.append(arr[i])
    start=time.time()
    sortari.shellSort(arr_de_sortat)
    timp=time.time() - start
    rez[3].append(timp)
    print(f"Timp shell sort: {timp}")

    #Heap sort
    start=time.time()
    sortari.heapSort(arr) #ultima sortare, deci putem folosi lista initiala
    timp=time.time() - start
    rez[4].append(timp)
    print(f"Timp heap sort: {timp}")
    #print(rez[test])

del arr
del arr_de_sortat

print(tests)
for i in rez:
    print(i)

Titlu=["Quick","Merge","Radix","Shell","Heap"]
teste = np.array([i for i in range(t)])
for i in range(5):
    plt.title(f"{Titlu[i]}sort")
    plt.xlabel("Test")
    plt.ylabel("Timp")
    plt.plot(teste,rez[i])
    plt.show()

plt.title("Toate sortarile")
plt.xlabel("Test")
plt.ylabel("Timp")
plt.plot(teste,rez[0])
plt.plot(teste,rez[1])
plt.plot(teste,rez[2])
plt.plot(teste,rez[3])
plt.plot(teste,rez[4])
plt.legend(["QuickSort","MergeSort","RadixSort","ShellSort","HeapSort"])
plt.show()


#Testele 1 si 2 luate din exemplu
#Testul 3 arata faptul ca radix sort este mai lent cu cat numerele sunt mai mari (a se compara cu testul 2)
#Testele 4 si 5 compara rapiditatea quick si merge.
#Testul 6 va crapa quick sortul prin multe apeluri recursive.
#Testul 7 va testa daca programul va ramane fara memorie sau nu.