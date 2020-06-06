import random
class MinHeap:
    def __init__(self,array):
        self.array=[]
        self.index=0
        self.heapify(array)
    def insert(self,value):
        self.array[self.index]=value
        if self.index!=0:
            pos_value=self.index
            while(self.array[pos_value]<self.array[int((pos_value-1)/2)]):
                self.array[pos_value],self.array[int((pos_value-1)/2)]=self.array[int((pos_value-1)/2)],self.array[pos_value]
                pos_value=int((pos_value-1)/2)
        self.index+=1
            
    def getKSmallest(self,k):
        array=[]*k
        for i in range(k):
            array.append(self.extract())
        for i in range(k):
            self.insert(array[i])
        return array
        
    def extract(self):
        extracted=self.array[0]
        self.array[0]=self.array[self.index-1]
        self.index-=1
        pos_value=0
        min=0
        while 1==1:
            self.array[pos_value],self.array[min]=self.array[min],self.array[pos_value]
            pos_value=min
            if 2*min+1>=self.index-1:
                min=2*min+1
            else:
                if 2*min+2<=self.index-1:
                    min = 2*min+1 if self.array[2*min+1]<=self.array[2*min+2] else 2*min+2
                else:
                    min=2*min+2
            if min>self.index-1 or self.array[pos_value]<=self.array[min]:
                break
        return extracted
    
    def print_heap(self):
        print(self.array[:self.index])
        
        
    def heap(self,array,i):
        lenA=len(array)
        min=i
        if 2*i+1<lenA and array[min]>array[2*i+1]:
            min=2*i+1
        if 2*i+2<lenA and array[min]>array[2*i+2]:
            min=2*i+2
        if i!=min:
            array[i],array[min]=array[min],array[i]
            self.heap(array,min)
        
    def heapify(self,array):
        for i in range(int(len(array)/2),-1,-1):
            self.heap(array,i)
        self.array=array
        self.index=len(array)       
            
            
        
#test implement HeapSort
array=random.sample(range(1, 100), 10)

tt=MinHeap(array)
tt.print_heap()
print(tt.getKSmallest(3))
tt.print_heap()
