import numpy as np
from SkipListOperations import SkipListOperations

#This file collects data for the number of operations
#for our Skip List implementation.
#
#1. This program writes the number of operations taken
#by the insert() function to insertData.txt.
#
#2. This program writes the number of operations taken
#by the search() function to searchData.txt.
#
#3. This program prints the average percent difference
#between the number of operations that the search() function 
#and insert() function take to the console.
if __name__ == '__main__':

    readNames = open("dataset.txt", "r")
    currentReader = readNames.readlines()

    insertFile = open("insertData.txt","w+")
    updateFile = open("searchData.txt","w+")

    numWords = 200
    dataPerWordInsert = np.zeros(numWords)
    dataPerWordUpdate = np.zeros(numWords)
    numTrials = 150
    percentDiff = 0
    averagePD = 0
    for current in range(0, numTrials): 
      index = 0
      testAnalysis = SkipListOperations()
      for i in currentReader:
            currentWord:str = i.capitalize()
            
            testAnalysis.insert(currentWord, currentWord)
            tempInsert = testAnalysis.count
            
            testAnalysis.search(currentWord)
            tempSearch = testAnalysis.count
            
            
            percentDiff += (tempInsert - tempSearch)/(tempSearch)
            
            dataPerWordInsert[index] += tempInsert
            dataPerWordUpdate[index] += tempSearch

            index += 1
      
      percentDiff /= index
      averagePD += abs(percentDiff)
     
    averagePD /= numTrials
    averagePD *= 100.0
    print('average percent difference: ' + str(averagePD))
    
    for j in range(0, numWords): 
       insertFile.write(str(dataPerWordInsert[j]/150.0) + "\n")
       updateFile.write(str(dataPerWordUpdate[j]/150.0) + "\n")
