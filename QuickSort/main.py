#Author: Marceus Jethro
#Implementation of QuickSort with average  time complexity of O(nlogn) and also with space complexity of
#O(n) in best cast and O(n^2) in worst case
#note that if you use the Partition fonction instead your space complexity will shrink
#to a constant but your time complexity will grow
#feel free to contact me if you detect any bugs
#n


import random
import time
#partitioning around the element A[leftIndex]
def Partition(A,pivot_index,left_index,right_index):
    correct_place=left_index+1
    for j in range(left_index+1,right_index+1):
        if A[pivot_index]>=A[j]:
            A[correct_place],A[j]=A[j],A[correct_place]
            correct_place+=1
    A[correct_place-1],A[pivot_index]=A[pivot_index],A[correct_place-1]
    return correct_place-1

#partitioning around any element but this use a worst case space complexity of O(n^2)
#and a best case space complexity of O(n) but i have the feeling its on average O(n) :D
#probably could be optimized 
def PartitionAny(A,pivot_index,left_index,right_index):
    copy=A[left_index:right_index+1]
    i=left_index
    j=right_index
    for k in range(0,right_index-left_index+1):
        if k+left_index==pivot_index:
            continue
        if copy[k]<=copy[pivot_index-left_index]:
            A[i]=copy[k]
            i+=1
        else:
            A[j]=copy[k]
            j-=1
    A[i]=copy[pivot_index-left_index]
    return i
            
    
def quickSort(Array,left_index,right_index,lenA):
    if lenA<=1:
        return 
    pivot=int(random.uniform(left_index,right_index))  #we use a uniform probabilty law to generate pivot
    #pivot=left_index   #if you want to use the partition function which always choose the left_index as pivot
    correct_place=PartitionAny(Array,pivot,left_index,right_index)
    quickSort(Array,left_index,correct_place-1,correct_place-1-left_index+1)
    quickSort(Array,correct_place+1,right_index,right_index-(correct_place+1)+1)
    
def runAlgo(Array):
    lenA=len(Array)
    left_index=0
    right_index=lenA-1
    quickSort(Array,left_index,right_index,lenA)
    
#test
array=random.sample(range(1, 100000000), 10000000)
start=time.time()
runAlgo(array)
print(time.time()-start)
            