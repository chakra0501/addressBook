import time
import numpy as np
from SkipListRuntime import SkipListRuntime

#This file collects data for the runtime
#for our Skip List implementation.
#
#1. This program writes the runtime of
#the insert() function to insertData.txt.
#
#2. This program writes the runtime of
#the search() function to searchData.txt.


if __name__ == '__main__':

    #read from files
    readNames = open("dataset.txt", "r")
    currentReader = readNames.readlines()

    insertFile = open("insertData.txt","w+")
    updateFile = open("searchData.txt","w+")

    dataPerWordInsert = np.zeros(200)
    dataPerWordUpdate = np.zeros(200)
    numSkipLists = 150  
    skipLists = []
    for j in range(0, numSkipLists):
        skipLists.append(SkipListRuntime()) 

    count = 0
    for i in currentReader:
        currentWord:str = i.capitalize()
        start = time.time()
        
        for k in range(0, numSkipLists):
            skipLists[k].insert(currentWord, currentWord)

        end = time.time()
        runtimeInsert = end-start
        dataPerWordInsert[count] += (runtimeInsert/numSkipLists)
    
        start2 = time.time()
        for z in range(0, numSkipLists):
            skipLists[z].search(currentWord)

        end2 = time.time()
        runtimeUpdate = end2-start2
        dataPerWordUpdate[count] += (runtimeUpdate/numSkipLists)

        count += 1



    for k in range (0, 200):
        insertFile.write(str(dataPerWordInsert[k]) + "\n")
        updateFile.write(str(dataPerWordUpdate[k]) + "\n")
