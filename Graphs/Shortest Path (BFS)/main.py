#Author Marceus Jethro
#implementation of a shortest path algorithm using breadth first search 

def SPBFS(graph,start,end):
    if start==end:
        return start
    queue=[start]
    viewed=[]
    found=0
    while(queue!=[]):
        node=queue.pop(0)
        viewed.append(node)
        for nd in graph[node]:
            if nd not in viewed:
                if nd==end:
                    viewed.append(end) #basicly all we have to do is return the viewed array if 
                    return viewed      #end==nd :D
                queue.append(nd)
    return [viewed,'this element is only reachable ']
                
                  
#test

graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A'],
    'D':['F','B'],  #dictionary where each node have a  list of adjacent node
    'E':['B'],
    'F':['D'],
    'G':['T'],
    'T':['W','S'],
    'S':['W'],
    'W':['T']
}

print(SPBFS(graph,'T','S'))
