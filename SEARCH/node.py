from collections import deque
import heapq
import copy


## Node class
class Node: 
    def __init__( self, state, parent=None, action=None, cost=0 ):
        self.state = state
        self.parent = parent  
        self.action = action  
        self.cost = cost  
        if parent is None:  
            self.depth = 0  
        else:
            self.depth = parent.depth + 1 

    def __hash__(self):
        if isinstance(self.state, list):
            return hash(tuple(map(tuple, self.state)))
        return hash(self.state)

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __gt__(self, other):
        return self.depth > other.depth
    
