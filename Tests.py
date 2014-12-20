'''
Created on Oct 21, 2014

@author: mury
'''

if __name__ == '__main__':
    pass
from Controller import *


def testAddNumber():
    testList=[]
    addNumber(testList,2)
    assert len(testList)==1
    addNumber(testList,5)
    assert len(testList)==2
testAddNumber()

def testInsertNumber():
    testList=[]
    insertNumber(testList,2,5)
    assert len(testList)==1
    insertNumber(testList,1,0)
    assert len(testList)==2
testInsertNumber()

def testRemoveNumber():
    testList=[1,2,3,4]
    removeNumber(testList,2)
    assert len(testList)==3
    removeNumber(testList,6)
    assert len(testList)==3
testRemoveNumber()

def testRemoveInterval():
    testList=[1,2,3,4,5,6]
    removeInterval(testList,2,4)
    assert testList==[1,2,6]
testRemoveInterval()

def testReplaceList():
    testList=[1,2,3,4,5,6,7,8]
    replaceList(l,[2,3],[10,11])
    assert testList==[1,10,11,4,5,6,7,8]
    
def testIsPrime():
    testList=[1,2,3,4,5,6,7,8]
    isPrime(testList,2,5)
    assert testList==[]