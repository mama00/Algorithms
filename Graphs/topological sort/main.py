#Author Marceus Jethro
#implementation of topological sort using a depth first search algorithm

def dfs(viewed,graph,start,lenA,sortedArray):
    for node in graph[start]:
        if node not in viewed:
            viewed.append(node)
            dfs(viewed,graph,node,lenA,sortedArray)
    sortedArray[lenA[0]]=start
    lenA[0]-=1
            
#test
def TopologicalSort(graph):
    LenArray=[int(len(graph))-1]
    sortedArray=['']*(LenArray[0]+1)
    viewed=[]
    for node in graph:
        if node not in viewed:
            dfs(viewed,graph,node,LenArray,sortedArray)
    return sortedArray
graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':['F'],  
    'E':['W'],
    'F':['E'],
    'W':[]
    
}

print(TopologicalSort(graph))
