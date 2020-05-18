#Author: Marceus Jethro
#Implementation of Number of inversion in a array using the Merge sort ideao
#feel free to contact me if you detect any bugs
def mergeAndNumberSplitInversion(a, b,lenA,lenB,oldNumberOfInversion):
    mergedList=[]
    i=0
    j=0
    numberOfInversion=oldNumberOfInversion
    for k in range(lenA+lenB):
        if a[i]>b[j]:
            mergedList.append(b[j])
            numberOfInversion+=lenA-i #each time inserting a b element there is (length of remaining A array) inversion
            j+=1
            if j==lenB:
                return [mergedList+a[i:],numberOfInversion]
            
        else:
            mergedList.append(a[i])
            i+=1
            if i==lenA:
                return [mergedList+b[j:],numberOfInversion] #if  one list have been totaly inserted just return inserted list + remaining                                      #return the insterted + the remaining
    return [mergedList,numberOfInversion]

def countNumberInversion(A,lenA):
    if lenA==1:
        return [A,0]
    firstPart=countNumberInversion(A[:int(lenA/2)],int(lenA/2))
    secondPart=countNumberInversion(A[int(lenA/2):],int(lenA/2) +lenA % 2)
    return mergeAndNumberSplitInversion(firstPart[0],secondPart[0],int(lenA/2),int(lenA/2 + lenA % 2),firstPart[1]+secondPart[1])

#test
array=[6,5,4,3,2,1]
print(countNumberInversion(array,int(len(array))))#list where element[0] is the sorted array element[1] is the number of inversion
            
    