#Author Marceus Jethro
#implementation of breadth first search algorithm

def BFS(graph,start):
    queue=[start]
    viewed=[]
    while(queue!=[]):
        node=queue.pop(0)
        viewed.append(node)
        for nd in graph[node]:
            if nd not in viewed:
                queue.append(nd)
    return viewed
                
                  
#test
graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A'],
    'D':['F','B'],  
    'E':['B'],
    'F':['D'],
    'G':['T'],
    'T':['W','S'],
    'S':['W'],
    'W':['T']
}

print(BFS(graph,'A'))
