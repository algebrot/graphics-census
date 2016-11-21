#Creates a graphics window
from graphics import *
width = 500
height = 400
title = 'Graphics Window'
win = GraphWin(title, width, height)
#Y-vals increase as you approach the top of the window
win.setCoords(0,0,width,height)

#A sample list I made to test the function
L = [5,6,12,3,47,25,9,31]
#Takes a list of numbers and draws a sequence of rectangles
def drawRectangles(numlist):
    x = 0
    #Goes through the list and draws equal-width rectangles spaced 50 units apart 
    for number in numlist:
        x = x + 50
        y = number
        pt1 = Point(x, y)
        pt2 = Point(x+5, 0)
        rect = Rectangle(pt1,pt2)
        rect.draw(win)
drawRectangles(L)
    


        
    


