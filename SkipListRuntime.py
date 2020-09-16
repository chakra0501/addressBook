from Node import Node
import numpy as np

#This class can be ran using AnalysisRuntime.py.
#Running this class using AnalysisRuntime.py will confirm 
#that the runtime data that we have collected shows a logarithmic trend.

#This class is an implementation of the Skip List
#data structure that has been modified to collect runtime data 
#of the search() and insert() methods.
#The main modification in this class is the
#presence of print statements at each operation 
#in the search() and insert() methods.
#We included these print statements because we were
#encountering a problem with the import called 'time', which
#we were using to collect runtime data.
#The problem was that the time import was rounding most 
#of our runtime data down to 0. The course staff suggested 
#that we include print statements at each operation to pad, or increase,
#the runtime of each operation by an (approximately) constant
#number so that the time import would not round our runtime data
#down to 0. 

class SkipListRuntime:
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
    def insert(self, personName, personEmail) :
        print("insert goes here")
        self.temp = None
        #get number of levels to insert at
        numLevels:int = self.getNumLevelsToInsertAt()
        print('inserting at ' + str(numLevels) + ' additional levels')
        #create new levels if necessary
        self.insertingNewLevels(numLevels)
        #start adding new contact to list
        tempInsertNode = self.head
        while (tempInsertNode is not None):
            print('at level ' + str(tempInsertNode.level))
            #only insert at levels that are less than or equal to numLevels
            if (tempInsertNode.nextNode is None) and tempInsertNode.name < personName:
                print('at node with name ' + str(tempInsertNode.name))
                if tempInsertNode.level <= numLevels:
                    print('found place at level ' + str(tempInsertNode.level))
                    self.createNewNode(tempInsertNode, None, personName, personEmail)
                print('moving down one level')
                tempInsertNode = tempInsertNode.downNode  

            elif tempInsertNode.name < personName and tempInsertNode.nextNode.name > personName:          
                print('at node with name ' + str(tempInsertNode.name))
                #insert node creator method here
                if tempInsertNode.level <= numLevels:
                    print('found place at level ' + str(tempInsertNode.level))
                    self.createNewNode(tempInsertNode, tempInsertNode.nextNode, personName, personEmail)
                print('moving down one level')
                tempInsertNode = tempInsertNode.downNode

            elif tempInsertNode.name < personName and tempInsertNode.nextNode.name < personName:
                print('at node with name ' + str(tempInsertNode.name))
                print('moving forward one node')
                tempInsertNode = tempInsertNode.nextNode
        

    def createNewNode(self, currentNode, nextNodeAfter, personName, personEmail):
        print("creating new node")
        
        print('inserted after ' + str(currentNode.name))

        if nextNodeAfter is not None:
            print('inserted before ' + str(nextNodeAfter.name))

        #create new node between the current node 
        #and the node right after the current node
        newNode:Node = Node(personName, personEmail, currentNode.level)
        newNode.nextNode = nextNodeAfter
        currentNode.nextNode = newNode

        
        if self.temp is not None:
            print('temp node has name ' + str(self.temp.name))
            self.temp.downNode = newNode
        
        print('setting temp node to node with name ' + str(newNode.name))
        self.temp = newNode



    def insertingNewLevels(self, numLevels):
        if numLevels > self.head.level:
            startInsertion:int = self.head.level + 1
            for i in range(startInsertion, numLevels + 2):
                newLevelNode:Node = Node("", "", i)
                newLevelNode.downNode = self.head
                self.head = newLevelNode
                print('created new head at level ' + str(self.head.level))


    
    def getNumLevelsToInsertAt(self) -> int:
        #return the number of coin flips
        #until a tail is flipped
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
        print("search goes here")

        nodeToReturn:Node = None
        tempFindNode = self.head
        found:bool = False
        while (tempFindNode is not None) and found == False:
            
            if tempFindNode.level == 0 and tempFindNode.name == personName:
                nodeToReturn = tempFindNode
                found = True
            
            elif (tempFindNode.nextNode is not None) and tempFindNode.name < personName and tempFindNode.nextNode.name <= personName:
                print("not yet found")
                print("going forward")
                tempFindNode = tempFindNode.nextNode
            
            else:
                print("not yet found")
                print("going downward")
                tempFindNode = tempFindNode.downNode

        return nodeToReturn
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
