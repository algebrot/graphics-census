#Creates a graphics window
from graphics import *
width = 500
height = 400
title = 'Graphics Window'
win = GraphWin(title, width, height)
#Y-vals increase as you approach the top of the window
win.setCoords(0,0,width,height)


#A sample list made to test the function
list1 = [("alice", 3), ("bob", 1), ("eve", 2)]
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
        y = 10 + pop[1]
        pt1 = Point(x, y)
        pt2 = Point(x+5, 100)
        rect = Rectangle(pt1,pt2)
        rect.draw(win)
        setpoint = Point((((x)+(x+5))/2), 0)
        txt = Text(setpoint, pop[0])
        txt.draw(win)
        
barChart(list1)
