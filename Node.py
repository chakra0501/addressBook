import Node

#This class represents a 
#single Node in a Skip List.

class Node:
    name:str
    email:str
    level:int
    nextNode:Node
    downNode:Node

    def __init__(self, name, email, level):
        self.name = name
        self.email = email
        self.level = level
        self.nextNode = None
        self.downNode = None
