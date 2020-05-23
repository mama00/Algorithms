#Author Marceus Jethro
#implementation of Random Selection
import random
#partitioning function
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

def RandomSelection(A,lenA,i):
    pivot=int(random.uniform(0,lenA-1))#randomly choosing the pivot
    position=PartitionAny(A,pivot,0,lenA-1)
    if position+1==i:
        return A[position]
    if position+1<i:
        return RandomSelection(A[position+1:lenA],lenA-position-1,i-position-1)
    else:
        return RandomSelection(A[0:position],position,i)
        
        
#test no check is set on i so you must choose a good value between 1 and lenght of A
array=[1,5,34,675,345,6,3,23,6,8]
print(RandomSelection(array,len(array),7))
    