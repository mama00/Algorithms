class Node:
    def __init__(self,value):
        self.value=value
        self.left_child=-1
        self.right_child=-1
        self.parent=-1
        
    def getValue(self):
        return self.value