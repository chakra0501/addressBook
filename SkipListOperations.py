from Node import Node
import numpy as np

#This class can be ran using AnalysisOperations.py.
#Running this class using AnalysisOperations.py will confirm 
#that the operations data we have collected shows that
#the insert() and search() methods need
#a similar number of operations to insert or find
#an element in the given dataset respectively.

#This class is an implementation of the Skip List
#data structure that has been modified to collect data
#about the number of operations that  
#the search() and insert() methods use when
#finding and inserting data into a Skip List.
#The main modification in this class is the
#presence of a new field, called 'count'.
#The 'count' field stores the number of operations that
#a single call to insert() or search() uses.
#Whenever we traverse over a node that in
#the Skip List on a single call to the insert()
#or search() methods, count is incremented by 1.

class SkipListOperations:
    head:Node
    temp:Node
    count:int
    #This class contains a field called count.
    #The field called 'count' stores the number
    #of operations needed for a single call
    #to the insert() or search() methods


    def __init__(self):
        self.head = Node("", "", 0)
        self.temp = None
        self.count = 0
    
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
        self.count = 0
        #Note how the count field is reset whenever we want to
        #insert a new contact.
        self.temp = None
        numLevels:int = self.getNumLevelsToInsertAt()
        self.insertingNewLevels(numLevels)
        tempInsertNode = self.head

        while (tempInsertNode is not None):
            
            if (tempInsertNode.nextNode is None) and tempInsertNode.name < personName:

                if tempInsertNode.level <= numLevels:
                    self.createNewNode(tempInsertNode, None, personName, personEmail)

                tempInsertNode = tempInsertNode.downNode
                if (tempInsertNode is not None) and tempInsertNode.level >= 0:
                    self.count += 1  

            elif tempInsertNode.name < personName and tempInsertNode.nextNode.name > personName:          
                if tempInsertNode.level <= numLevels:
                    self.createNewNode(tempInsertNode, tempInsertNode.nextNode, personName, personEmail)

                tempInsertNode = tempInsertNode.downNode
                if (tempInsertNode is not None) and tempInsertNode.level >= 0:
                    self.count += 1

            elif tempInsertNode.name < personName and tempInsertNode.nextNode.name < personName:
                tempInsertNode = tempInsertNode.nextNode
                self.count += 1
       


    def createNewNode(self, currentNode, nextNodeAfter, personName, personEmail):
        newNode:Node = Node(personName, personEmail, currentNode.level)
        newNode.nextNode = nextNodeAfter
        currentNode.nextNode = newNode
        
        if self.temp is not None:
            self.temp.downNode = newNode
        
        self.temp = newNode



    def insertingNewLevels(self, numLevels):
        if numLevels > self.head.level:
            startInsertion:int = self.head.level + 1 
            for i in range(startInsertion, numLevels + 2):
                #self.count += 1
                newLevelNode:Node = Node("", "", i)
                newLevelNode.downNode = self.head
                self.head = newLevelNode

    
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
        #Note how the count field is reset whenever we want to
        #find an existing contact.
        nodeToReturn:Node = None
        tempFindNode = self.head
        found:bool = False
        while (tempFindNode is not None) and found == False:
            
            if tempFindNode.level == 0 and tempFindNode.name == personName:
                nodeToReturn = tempFindNode
                found = True
            
            elif (tempFindNode.nextNode is not None) and tempFindNode.name < personName and tempFindNode.nextNode.name <= personName:
                tempFindNode = tempFindNode.nextNode
                self.count += 1
            
            else:
                tempFindNode = tempFindNode.downNode
                if (tempFindNode is not None) and tempFindNode.level >= 0:
                    self.count += 1
        return nodeToReturn
