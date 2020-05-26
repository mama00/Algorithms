#Author Marceus Jethro
#implementation of a deep first search algorithm
def DFS(graph,start):
    viewed=[start]
    dfs_sub(viewed,graph,start)
    return viewed

def dfs_sub(viewed,graph,start):
    for node in graph[start]:
        if node not in viewed:
            viewed.append(node)
            dfs_sub(viewed,graph,node)       
            
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

print(DFS(graph,'A'))
