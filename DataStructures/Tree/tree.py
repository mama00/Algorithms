import node
class Tree:
    def __init__(self,node):
        self.node=node
        
    
    def insertion_in_tree(self,parent,node):
        if parent.value>=node.value:
            if parent.left_child==-1:
                parent.left_child=node
                node.parent=parent
            else:
                self.insertion_in_tree(parent.left_child,node)
        elif parent.value<=node.value:
            if parent.right_child==-1:
                parent.right_child=node
                node.parent=parent
            else:
                self.insertion_in_tree(parent.right_child,node)
        
    def insert(self,node):
        self.insertion_in_tree(self.node,node)
        
    def search(self,value,parent=0):
        if parent==0:
            parent=self.node
        while parent.value!=value:
            if parent.value>value:
                if parent.left_child!=-1:
                    return self.search(value,parent.left_child)
                else:
                    return -1
            else:
                if parent.right_child!=-1:
                    return self.search(value,parent.right_child)
                else:
                    return -1
        if parent.value==value:
            return parent
                
    def printTree(self,node=0):
        if node==0:
            node=self.node
        print(node.value)
        if node.left_child!=-1:
            self.printTree(node.left_child)
        if node.right_child!=-1:
            self.printTree(node.right_child)
            
    def getPredecessor(self,node=0):
        cpn=node
        if node==0:
            node=self.node.left_child
        else:
            node=node.left_child
        if node!=-1:
            def getPSub(node):
                while node!=-1 and node.right_child!=-1:
                    return getPSub(node.right_child)
                return node
            return getPSub(node)
        else:
            if cpn.parent!=-1:
                def getPsub(node):
                    while node.parent!=-1 and node.parent.right_child!=-1 and node.parent.right_child!=node:
                        return getPsub(node.parent)
                    return node.parent
                return getPsub(cpn)
            else:
                return -1
            
        
            
            
    def delete(self,value):
        node=self.search(value)
        if node!=-1:
            pred=self.getPredecessor(node)
            if pred!=-1:
                if pred.parent.left_child==pred:
                    pred.parent.left_child=pred.left_child
                else:
                    pred.parent.right_child=pred.left_child
                if node.parent.left_child==node:
                    node.parent.left_child=pred
                else:
                    node.parent.right_child=pred
                if node.left_child!=-1:
                    node.left_child.parent=pred
                    pred.left_child=node.left_child
                else:
                    pred.left_child=-1
                if node.right_child!=-1:
                    node.right_child.parent=pred
                    pred.right_child=node.right_child
                else:
                    pred.right_child=-1
            else:
                print('Cant delete  the only one remaining element')
        else:
            print('Cant find this node')
        
    def printOrder(self,node=0):
        if node==0:
            node=self.node
        if node.left_child!=-1:
            self.printOrder(node.left_child)
        print(node.value)
        if node.right_child!=-1:
            self.printOrder(node.right_child)
                
                
            
                    
                
                