'''
Created on Oct 21, 2014

@author: mury
'''
#from Crypto.Util.number import GCD

if __name__ == '__main__':
    pass

'''A math teacher needs a program in order to help students to test different properties of numbers. The
program manages a list of numbers and also allows students to repeatedly execute the following
functionalities (each functionality is exemplified):

1. Add numbers into the list.
a. add 123 – adds 123 at the end of the list
b. insert 123 at 1 – insert number 123 at position 1 in the list; positions are numbered from 0.

2. Modify elements from the list.
a. remove 1 – removes the element at position 1.
b. remove from 1 to 3 – removes the elements at positions 1,2, and 3.
c. replace 1 3 5 with 5 3 – replaces all the occurrences of sublist 1 3 5 with the sublist 5 3.

3. Write the numbers having different properties.
a. prime from 1 to 5 – writes the prime numbers between position 1 and 5 in the list.
b. odd from 1 to 5 – writes the odd numbers between position 1 and 5 in the list. 

4. Obtain different characteristics of sublists.
a. sum from 1 to 5 – writes the sum numbers between position 1 and 5 in the list.
b. gcd from 1 to 5 - writes the greatest common divisor of elements between position 1 and
5 in the list.
c. max from 1 to 5 – writes the greater element of the sublist from position 1 to 5.

5. Filter.
a. filter prime – retains only the prime numbers.
b. filter negative –retains only the negative numbers.

6. Undo the last operation.
a. undo – the last operation that has modified the list of numbers is cancelled'''

from math import sqrt

l=[]
def addNumber(l,num):        #Adds the number num into the list l.
    l.append(num)
def insertNumber(l,pos,num):        #Inserts the number num to the position pos into the list l.
    l.insert(pos,num)
def removeNumber(l,pos):        #Removes the number at the position pos into the list.
    if pos<len(l):          #Checks if pos is in the list.
        l.pop(pos)
def removeInterval(l,num1,num2):        #Removes the numbers from num1 to num2 into the list.
    del l[num1:num2+1]    
def replaceList(l,target,replacement):       #Replace the numbers from target with the numbers from replacement into the list.
    result=[l.index(item) for item in target]           #Result retains the index of target.
    uhu=len(target)-1           #Retains the len of the target minus 1.
    l[result[0]:result[uhu]+1]=replacement           #Slice the l list with the index of target and replace with the replacement elements.
def removeOdd(l,num1,num2):              #Return the odd numbers from num1 to num2 into the list.
    l=l[num1:num2]              #Slice the list to be only from num1 to num2.
    return [x for x in l if x % 2 != 0]                 #Return numbers only if there are not divisible by 2.
def isPrime(l,num1,num2):               #Return the prime list from num1 to num2.
    l=l[num1:num2]                   #Slices the list to be only from num1 to num2.
    return [x for x in range(2,len(l)) if not [y for y in range(2, int(sqrt(x))+1) if x%y ==0]] #Returns the prime numbers.

    