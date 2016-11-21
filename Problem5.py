#Creates a graphics window
from graphics import *
width = 400
height = 500
title = 'Graphics Window'
win = GraphWin(title, width, height)
#Y-vals increase as you approach the top of the window
win.setCoords(0,0,width,height)

#Takes in the name of a pop data file and returns a list of tuples
def getListFromFile(filename):
    inputFile = open(filename)
    lst = []
    for line in inputFile:
        #each tuple contains a city, state, and pop value
        (city, state, population_string) = line.split(',')
        population = int(population_string)
        tup = (city, state, population)
        lst.append(tup)
    return lst
poplist = getListFromFile("/Users/coracoleman/Desktop/CensusData2014")

from heapq import nlargest

#Takes a list of tuples, a state input, and a Nth number N and returns a tuple
#of the Nth largest city population in the input state
def NthLargestCity(tuplist, desiredState, N):
    newpop = []
    for item in tuplist:
        state = item[1]
        if state == desiredState:
            pop = (item[2])
            newpop.append(pop)
    Z=sorted(newpop,reverse=True)
    Nth = Z[N-1]
    for item in tuplist:
        if item[2] == Nth:
            print (item[0])
            print (item[1])
            print (item[2])
            return((item[0],item[2]))

print(NthLargestCity(poplist, 'Florida', 5))
print(NthLargestCity(poplist, 'Florida', 4))
print(NthLargestCity(poplist, 'Florida', 3))
print(NthLargestCity(poplist, 'Florida', 2))
print(NthLargestCity(poplist, 'Florida', 1))

newertup = [("St. Petersburg city", 253693), ("Orlando city", 262372), ("Tampa city", 358699), ("Miami city", 430332), ("Jacksonville city", 853382)]

#Takes a list of tuples and draws rectangles based off height values
def barChart(tuplist):
    x = 0
    #makes a copy of the list 
    copytuplist = list(tuplist)
    #finds max number
    big = 0
    for pop in tuplist:
        if pop[1] > big:
            big = pop[1]
    #goes through the list and draws equal-width rectangles spaced 50 units apart
    for pop in tuplist:
        #divide number by max number
        pop[1]/big
        #multiply by the scaling factor
        pop[1]*big
        x = x + 150
        y = pop[1]
        pt1 = Point(x, y)
        pt2 = Point(x+5, 100)
        rect = Rectangle(pt1,pt2)
        rect.draw(win)
        setpoint = Point((((x)+(x+5))/2), 0)
        txt = Text(setpoint, pop[0])
        txt.draw(win)
        
barChart(newertup)
#Window not big enough for display*


