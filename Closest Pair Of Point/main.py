#Author: Marceus Jethro
#Implementation of Closest pair of point Algorithm with O(nlog(n)) time complexity
#note that all point have to be distinct
#feel free to contact me if you detect any bugs
#n

##################Our Sort algorithm for point##############################################
import math
def merge(a, b,lenA,lenB,by):
    mergedList=[]
    i=0
    j=0
    for k in range(lenA+lenB):
        if a[i][by]>b[j][by]:
            mergedList.append(b[j])
            j+=1
            if j==lenB:
                return mergedList+a[i:]
            
        else:
            mergedList.append(a[i])
            i+=1
            if i==lenA:
                return mergedList+b[j:]
    return mergedList

def mergeSort(A,lenA,by):
    if lenA==1:
        return A
    firstPart=mergeSort(A[:int(lenA/2)],int(lenA/2),by)
    secondPart=mergeSort(A[int(lenA/2):],int(lenA/2) +lenA % 2,by)
    return merge(firstPart,secondPart,int(lenA/2),int(lenA/2 + lenA % 2),by)
##############################################################################


def distance(p,q):
    return math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)
#now the business

#the idea here is to check for each point X in the left side we determine if their distance from the middle
#is < to the minimum distance delta and if it is we search where that point is in the sortedByY array
#when we find it we look 4 point before and 4 point after to see if there is a minimum smaller than delta
#but I also noticed that if the distance of the point X is greater than delta/2 whe only need to look at 2 point
#before and two point after


#return ([(p1x,p1y),(p2x,p2y),distance(p1,p2)])
def computeMiddle(sortedByX,sortedByY,delta,lenA):
    maxIndex=4
    lefIndex=0# just for avoiding index overflow in array
    rightIndex=0
    for i in range(int(lenA/2)-1,0,-1):
        if sortedByX[int(lenA/2)][0]-sortedByX[i][0]>delta[2]:
            break;
        if sortedByX[int(lenA/2)][0]-sortedByX[i][0]>delta[2]/2:
            maxIndex=2
        indexInY=sortedByY.index((sortedByX[i][0],sortedByX[i][1]))
        
        if indexInY-maxIndex<0:
            leftIndex = indexInY
        else:
            leftIndex= maxIndex
        if lenA-indexInY<=maxIndex:
            rightIndex=lenA-indexInY-1
        else:
            rightIndex=maxIndex
        for j in range(indexInY-lefIndex,indexInY+rightIndex):
            if j==indexInY:
                continue;
            dd=distance(sortedByY[indexInY],sortedByY[j])
            if dd<delta[2]:
                delta=[sortedByY[j],sortedByY[indexInY],dd]
    return delta
                
#return ([(p1x,p1y),(p2x,p2y),distance(p1,p2)])
def ClosestPair(sortedByX,sortedByY,lenA):
    #if lenA ==2 or 3 we brute force it
    if lenA==2:
        return [sortedByX[0],sortedByX[1],distance(sortedByX[0],sortedByX[1])]
    
    if lenA==3:
        pair=[sortedByX[0],sortedByX[1]]
        d1=distance(sortedByX[0],sortedByX[1])
        d2=distance(sortedByX[0],sortedByX[2])
        if d2<d1:
            pair=[sortedByX[0],sortedByX[2]]
            d1=d2
        d3=distance(sortedByX[1],sortedByX[2])
        if d3<d1:
            pair=[sortedByX[1],sortedByX[2]]
            d1=d3
        return [pair[0],pair[1],d1]
        
    leftPart=ClosestPair(sortedByX[:int(lenA/2)],sortedByY[:int(lenA/2)],int(lenA/2))
    rightPart=ClosestPair(sortedByX[int(lenA/2):],sortedByY[int(lenA/2):],int(lenA/2) +lenA % 2)
    delta=0 #minimum 
    if leftPart[2]<rightPart[2]:
        delta=leftPart
    else:
        delta=rightPart
    # whe compute the minimum in the first half of point sortedbyX and in the second half
    #then we check if there isnt a minimum where one point is on left side and one point in the 
    #right side
    return computeMiddle(sortedByX,sortedByY,delta,lenA)
        
        

def runAlgo(A):
    lenA=int(len(A))
    sortedByX=mergeSort(A,lenA,0)
    sortedByY=mergeSort(A,lenA,1)
    result=ClosestPair(sortedByX,sortedByY,lenA)
    return result;
    
    
#test

C=[(54,65),(96,103),(102,154),(3,4),(181,109),(0,0),(0.3,0.2),(242,31),(235,93),(3,3),(4,5),(1,1),(133,66)]

print(runAlgo(C))