import numpy as np
from SkipList import SkipList
from Node import Node

def printPromptMessage():
    print("Type 'add' to add a new contact to your address book")
    print("Type 'update' to update the information of an existing contact")
    print("Type 'exit' to exit your address book application")

if __name__ == '__main__':
    current = SkipList()
    print("Welcome message here")
    printPromptMessage()
    userInput:str = input("Your input: ")
    while (userInput != "exit"):
        if (userInput == "add"):
            print("Type the name of the person you want to add: ")
            personName:str = input("")
            while len(personName) == 0:
                print("The person's name cannot have no characters.")
                print("Please retype the name of you contact: ")
                personName = input("")
            print("Type the email of the person you want to add: ")
            personEmail:str = input("")
            foundNode:Node = current.search(personName.capitalize())
            if (foundNode == None):
                current.insert(personName.capitalize(), personEmail)
                print('Added ' + str(personName) + ' to the contact book.')
            else:
                print(str(personName) + ' is already in the contact book. ')

        if (userInput == "update"):
            print('Type the name of the contact whose information you want to update:')
            name:str = input("")
            foundNode:Node = current.search(name.capitalize())
            if (foundNode == None):
                print("The person you tried to find does not exist in your contacts.")
                print("Would you like to add this person to your contacts?")
                print("Please type 'Yes' if you want to add them.")
                print("Please type 'No' otherwise. ")
                response:str = input("")
                if response == "Yes":
                     print("Type the email of the person you want to add: ")
                     personEmail:str = input("")
                     current.insert(name, personEmail)
                     print(str(name) + ' has been added to the contact book.')

            else:
                print("name found:", foundNode.name)
                print("email found:", foundNode.email)
                print('would you like to change the email of ' + foundNode.name + '? ')
                print("Please type 'Yes' if you want to change their email. ")
                print("Please type 'No' otherwise. ")
                changeOrNot:str = input("")
                if changeOrNot == "Yes":
                    print("Type in the new email: ")
                    newEmail:str = input("")
                    foundNode.email = newEmail

        printPromptMessage()
        userInput = input("Your input: ")
