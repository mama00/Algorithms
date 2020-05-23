#Author Marceus Jethro
#implementation of Determinist Selection Algorithm which is a determinist variant of random selection
#it run in O(n) 
import mergeSort
import random
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

def DeterministSelection(A,lenA,i):
    if lenA<5:
        sortedArray=mergeSort.mergeSort(A,lenA)
        return sortedArray[i-1]
    
####################################################################
#this compute the median. In the random selection all this block is replaced by int(random.random(0,lenA-1))
    medians_array=[]
    #round up the nomber of groups when its not an integer
    number_of_groups=int(lenA/5)
    if int(lenA/5)<lenA/5:
        number_of_groups+=1
    for k in range(0,number_of_groups):
        end=0
        if k*5+5>=lenA:
            end=lenA
        else:                                #detecting end of array
            end=k*5+5 
        sortedArray=mergeSort.mergeSort(A[k*5:end],end-k*5)
        middle=int((end-k*5)/2)
        medians_array.append(sortedArray[middle])   
    pivot=DeterministSelection(medians_array,number_of_groups,int(number_of_groups/2 ))#we get the value but we need index
    pivot=A.index(pivot)#index of pivot
    ############################################################################################################3
    position=PartitionAny(A,pivot,0,lenA-1)
    if position+1==i:
        return A[position]
    if position+1<i:
        return DeterministSelection(A[position+1:lenA],lenA-position-1,i-position-1)
    else:
        return DeterministSelection(A[0:position],position,i)
        
        
#test no check is set on i so you must choose a good value between 1 and lenght of A
array=[1,5,34,675,345,6,3,23,6,8]
print(DeterministSelection(array,len(array),7))
    