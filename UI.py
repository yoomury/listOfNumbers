'''
Created on Oct 25, 2014

@author: MuRy
'''

if __name__ == '__main__':
    pass
from Controller import *

def printOptions():             #Prints the menu.
    print("1. Add numbers into the list. \n\
2. Modify elements from the list. \n\
3. Write the numbers having different properties. \n\
4. Obtain different characteristics of sublists. \n\
5. Filter. \n\
6. Undo.")

def mainMenu():
    printOptions()
    cmd=int(input("Please enter an option: "))  #Check your option.
    if cmd==1:
        ui1()
    if cmd==2:
        ui2()
    if cmd==3:
        ui3()
    if cmd==4:
        ui4()
    if cmd==5:
        ui5()
    if cmd==6:
        ui6()


def ui1(): #The first sub-menu.
    print("1. Add a number at the end of the list. \n\
2. Insert a number at a specific position. \n\
3. Print the list \n\
4. Main Menu.")
    cmd=int(input("Please enter an option: "))  #Converts cmd to int
    if cmd==1:
        while True:
            try: 
                num=int(input("Please enter the desire number (press any non numerical value to go back): "))
                addNumber(l,num)
            except ValueError: #If a non numerical value was inputed then prints again the sub-menu.
                ui1()
    
    if cmd==2:
        while True:
            try:
                num=int(input("Please enter the desire number (press any non numerical value to go back): "))
            except ValueError:  #If a non numerical value was inputed then prints again the sub-menu.
                ui1()
            try:
                pos=int(input("Please enter the desire position (press any non numerical value to go back): "))
                insertNumber(l,pos,num)
            except ValueError:  #If a non numerical value was inputed then prints again the sub-menu.
                ui1()
    if cmd==3: #Prints the list.
        print(l)
        input("Press any key to go back")
        mainMenu()    
    if cmd==4:  #Goes back to the main menu
        mainMenu()     

def ui2():  #The second sub-menu.
    print("1. Remove the element at the desired position. \n\
2. Remove the elements from a desired interval. \n\
3. Replace all the occurrences of a sublist with a different sublist. \n\
4. Print the list. \n\
5. Main Menu.")
    cmd=int(input("Please enter an option: "))  #Converts cmd to int
    if cmd==1:
        while True:
            try:
                pos=int(input("Please enter the desire position (press any non numerical value to go back): "))
                if pos>len(l)-1:
                    raise IndexError #Raise IndexError if pos not in list.
            except IndexError:  #Raise an input error
                opt=input("You don't have that position in your list, do yo want to edit it? y/n")
                if opt=='y': #Goes back to the sub-menu 1 to edit the list.
                    ui1()
                if opt=='n': #Break
                    break
            except ValueError: #If a non numerical value was inputed then prints again the sub-menu.
                ui2()
            removeNumber(l,pos)
    if cmd==2:
        while True:
            try:
                num1=int(input("Please enter the first number of the interval (press any non numerical value to go back): "))
                num2=int(input("Please enter the last number of the interval (press any non numerical value to go back): "))
                if (num1<0) or (num2>len(l)-1): #If num1 or num2 not in the list raise IndexError
                    raise IndexError
            except IndexError: #Raise an input error
                opt=input("You don't have that position in your list, do yo want to edit it? y/n")
                if opt=='y':    #Goes back to the sub-menu 1 to edit the list.
                    ui1()
                if opt=='n':    #Goes back to the sub-menu.
                    ui2()
            except ValueError:  #If a non numerical value was inputed then prints again the sub-menu.
                ui2()
            removeInterval(l,num1,num2)
    if cmd==3:
        target=[]       #The list that holds the target elements.
        replacement=[]      #The list that holds the replacement elements.
        try:
            while True:
                try:
                    num1=int(input("Please insert the numbers of the target sublist (press any non numerical value to go further): "))
                    if num1 in l:   #If num1 in l then appends num1 to target list.
                        target.append(num1)
                    else:
                        raise IndexError    #IndexError, if num1 not in the list.
                except ValueError:  #If a non numerical value was inputed then prints again the sub-menu.
                    break
            while True:
                try:
                    num2=int(input("Please insert the numbers of the replacement sublist (press any non numerical value to go further): "))
                    '''if num2 in l:   #If num2 in l then appends num2 to replacement list.'''
                    replacement.append(num2)
                    '''else:
                        raise IndexError #IndexError, if num2 not in the list.'''
                except ValueError:  #If a non numerical value was inputed then prints again the sub-menu.
                    break
        except IndexError:  #Raise an input error message.
            opt=input("You don't have that numbers in your list, do yo want to edit it? y/n")
            if opt=='y':    #Goes back to the sub-menu 1 to edit the list.
                ui1()
            if opt=='n':    #Goes back to the sub-menu
                ui2()
        replaceList(l,target,replacement)
        ui2()
    if cmd==4:
        print(l)    #Prints the list.
        input("Press any key to go back")
        mainMenu()    
    if cmd==5:  #Goes back to the main menu.
        mainMenu()  
        

def ui3():
    print("1. Write the prime numbers between two desired positions. \n\
2. Write the odd numbers between two desired positions. \n\
3. Print the list. \n\
4. Main menu.")
    cmd=int(input("Please enter the desired position: "))
    global l
    if cmd==1:
        while True:
            try:
                try:
                    num1=int(input("Please enter the first number of the interval (press any non numerical value to go back: "))
                    if num1 in l: #Checks if num1 is in the list or not.
                        return
                    else:   #Raise IndexError if not.
                        raise IndexError
                except ValueError:  #If a non numerical value was inputed then prints again the sub-menu.
                    ui3()
                try:
                    num2=int(input("Please enter the last number of the interval (press any non numerical value to go back): "))
                    if num2 in l:   #Checks if num2 is in the list or not.
                        return
                    else:   #Raise IndexError if not.
                        raise IndexError
                except ValueError:  #If a non numerical value was inputed then prints again the sub-menu.
                    ui3()
            except IndexError:  #Raise an inputed error message.
                opt=input("You don't have that numbers in your list, do yo want to edit it? y/n")
                if opt=='y':    #Goes back to the sub-menu 1 to edit the list.
                    ui1()
                if opt=='n':    #Goes back to the sub-menu.
                    ui3()
            l=isPrime(l,num1,num2)
            ui3()
    if cmd==2:
        try:
            try:
                num1=int(input("Please enter the first number of the interval (press any non numerical value to go back): "))
                if num1 in l: #Checks if num1 is in the list or not.
                    return
                else:   #Raise IndexError if not.
                    raise IndexError
            except ValueError:  #If a non numerical value was inputed then prints again the sub-menu.
                ui3()
            try:
                num2=int(input("Please enter the last number of the interval (press any non numerical value to go back): "))
                if num2 in l:   #Checks if num2 is in the list or not.
                    return
                else:   #Raise IndexError if not.
                    raise IndexError
            except ValueError:  #If a non numerical value was inputed then prints again the sub-menu.
                ui3()
        except IndexError:  #Raise an inputed error message.
            opt=input("You don't have that numbers in your list, do yo want to edit it? y/n")
            if opt=='y':    #Goes back to the sub-menu 1 to edit the list.
                ui1()
            if opt=='n':    #Goes back to the sub-menu.
                ui3()
        l=removeOdd(l,num1,num2)
        ui3()
    if cmd==3:  #Prints the list.    
        print(l)
        input("Press any key to go back")   
    if cmd==4:  #Goes back to the main menu.
        mainMenu()

def ui4(): #Not yet implemented.
    print("Not yet implemented")
    mainMenu()
def ui5():  #Not yet implemented.
    print("Not yet implemented")
    mainMenu()
def ui6():  #Not yet implemented.
    print("Not yet implemented")
    mainMenu()
    
mainMenu()