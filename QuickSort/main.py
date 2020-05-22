#Author: Marceus Jethro
#Implementation of QuickSort with average  time complexity of O(nlogn) and also with space complexity of
#O(nlogn)

#note that if you use the Partition fonction instead your space complexity will shrink
#to a constant but your time complexity will grow
#feel free to contact me if you detect any bugs
#n


import random
#partitioning around the element A[leftIndex]
def Partition(A,pivot_index,left_index,right_index):
    correct_place=left_index+1
    for j in range(left_index+1,right_index+1):
        if A[pivot_index]>=A[j]:
            A[correct_place],A[j]=A[j],A[correct_place]
            correct_place+=1
    A[correct_place-1],A[pivot_index]=A[pivot_index],A[correct_place-1]
    return correct_place-1

#partitioning around any element but this use a space complexity of O(nlogn)
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
    print(Array)
    
#test
array=[2,333,35,53,35,33,5,23,53,55,66,23,756,23,2345,43,987,564,77,87,343,234,56,7687,9987,345,754,4637,245,654]
runAlgo(array)
            