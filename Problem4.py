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

#Takes in poplist from the above function and returns the total pop of the input state
def sumState(inputlist, desiredState):
    poplist = []
    #goes through the list 
    for item in inputlist:
        state = item[1]
        #if the input state =s the state in the tuple
        if state == desiredState:
            pop = item[2]
            poplist.append(pop)
    total = sum(poplist)    
    return total
total = sumState(poplist, 'NewYork')
print(total)

#Cali total = 26756002
#Fl total = 6824587
#NY total = 9891315
#Texas total = 14322328

#Using values produced from sumState, I created a new tuplist to input into 
newtup = [("California", 26756002), ("Florida", 6824587), ("NewYork", 9891315), ("Texas", 14322328)] 

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
        x = x + 50
        y = pop[1]
        pt1 = Point(x, y)
        pt2 = Point(x+5, 100)
        rect = Rectangle(pt1,pt2)
        rect.draw(win)
        setpoint = Point((((x)+(x+5))/2), 0)
        txt = Text(setpoint, pop[0])
        txt.draw(win)
        
barChart(newtup)
#Window not big enough for display*






