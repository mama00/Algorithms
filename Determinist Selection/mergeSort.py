#Author: Marceus Jethro
#Implementation of Merge sort algorithm
#feel free to contact me if you detect any bugs
def merge(a, b,lenA,lenB):
    mergedList=[]
    i=0
    j=0
    for k in range(lenA+lenB):
        if a[i]>b[j]:
            mergedList.append(b[j])
            j+=1
            if j==lenB:
                return mergedList+a[i:]
            
        else:
            mergedList.append(a[i])
            i+=1
            if i==lenA:
                return mergedList+b[j:] #if  one list have been totaly inserted just return inserted list + remaining                                      #return the insterted + the remaining
    return mergedList

def mergeSort(A,lenA):
    if lenA==1:
        return A
    firstPart=mergeSort(A[:int(lenA/2)],int(lenA/2))
    secondPart=mergeSort(A[int(lenA/2):],int(lenA/2) +lenA % 2)
    return merge(firstPart,secondPart,int(lenA/2),int(lenA/2 + lenA % 2))

        
            
    