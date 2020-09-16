from Node import Node
import numpy as np

#This class can be ran using driver.py.
#Running this class using driver.py will confirm 
#that our implementation of the 
#Skip List data structure works.

class SkipList:
    head:Node
    temp:Node


    def __init__(self):
        self.head = Node("", "", 0)
        self.temp = None
    
    #The insert method adds a new contact 
    #(represented by a new node) to the
    #Skip List.
    #
    #Parameters:
    #1. Takes a String representing the name of the contact 
    #we want to insert into the Skip List.
    #2. Takes a String representing the email of the contact 
    #we want to insert into the Skip List.
    #
    #Returns: no return value.
    def insert(self, personName, personEmail):
        self.temp = None
        #get the number of levels to insert the new contact at 
        numLevels:int = self.getNumLevelsToInsertAt()
        #create any additional levels if necessary
        self.insertingNewLevels(numLevels)
        tempInsertNode = self.head

        while (tempInsertNode is not None):
            
            #if we want to place the new contact 
            #at the end of the list of nodes at a given level
            if (tempInsertNode.nextNode is None) and tempInsertNode.name < personName:
                #if we are a level less than or equal to
                #the number of levels that we will insert the contact
                #at, create a new node to represen the new contact
                if tempInsertNode.level <= numLevels:
                    self.createNewNode(tempInsertNode, None, personName, personEmail)

                #traverse down 1 level
                tempInsertNode = tempInsertNode.downNode

            #if we want to place the new contact at in the middle of the list of nodes at a given level
            elif tempInsertNode.name < personName and tempInsertNode.nextNode.name > personName: 
                 #if we are a level less than or equal to
                #the number of levels that we will insert the contact
                #at, create a new node to represen the new contact        
                if tempInsertNode.level <= numLevels:
                    self.createNewNode(tempInsertNode, tempInsertNode.nextNode, personName, personEmail)
                
                #traverse down 1 level
                tempInsertNode = tempInsertNode.downNode

            #if we have not found the correct place to insert the new contact at a given level
            elif tempInsertNode.name < personName and tempInsertNode.nextNode.name < personName:
                #traverse forward 1 node
                tempInsertNode = tempInsertNode.nextNode
       

    #create a new node between the current node, given by currentNode, and the 
    #node after the current node, given by nextNodeAfter
    def createNewNode(self, currentNode, nextNodeAfter, personName, personEmail):
        #personName and personEmail represent the name and email of the new contact
        newNode:Node = Node(personName, personEmail, currentNode.level)
        newNode.nextNode = nextNodeAfter
        currentNode.nextNode = newNode
        
        if self.temp is not None:
            self.temp.downNode = newNode
        
        self.temp = newNode


    #creating new levels if the current number 
    #of levels is less than the number of levels
    #that we want to insert the new contact at
    def insertingNewLevels(self, numLevels):
        if numLevels > self.head.level:
            startInsertion:int = self.head.level + 1 
            for i in range(startInsertion, numLevels + 2):
                newLevelNode:Node = Node("", "", i)
                newLevelNode.downNode = self.head
                self.head = newLevelNode

    
    #simulates a set of coin flips and returns
    #the number of consecutive "heads" flipped 
    #in a row
    def getNumLevelsToInsertAt(self) -> int:
        probHeads:float = 0.5
        count:int = 0
        while np.random.rand() < probHeads:
            count += 1
        return count

    #The search method finds an existing contact 
    #(represented by a single node) to the
    #Skip List.
    #
    #Parameters:
    #1. Takes a String representing the name of the contact 
    #we want to insert into the Skip List.
    #
    #Returns: 
    #If there is a node in the Skip List containing the
    #name of the contact that we are looking for, return that node.
    #Else, return None.
    def search(self, personName):
        self.count = 0
        nodeToReturn:Node = None
        tempFindNode = self.head
        found:bool = False
        
        while (tempFindNode is not None) and found == False:
            
            #if we are at the lowest level and the current node has the same name 
            #as the name we are looking for, return the current node
            if tempFindNode.level == 0 and tempFindNode.name == personName:
                nodeToReturn = tempFindNode
                found = True
            
            #if the current node and the next node in front of 
            #it have names that are alphabetically ahead
            #of the contact we are looking for, 
            #traverse forward by 1 node
            elif (tempFindNode.nextNode is not None) and tempFindNode.name < personName and tempFindNode.nextNode.name <= personName:
                tempFindNode = tempFindNode.nextNode
            
            #traverse down 1 level in all other cases
            else:
                tempFindNode = tempFindNode.downNode

        return nodeToReturn

