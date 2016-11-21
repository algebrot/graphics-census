Workshop Assignment #9
This assignment is due on November 19 (at 10:30am)

For this assignment, we will once again use a graphics package was created by John Zelle. There is no single best graphics package for Python. Different people have written different graphics packages, and you will find that certain packages are designed with different goals in mind.

You can find a brief overview of the graphics package in the write­up for Workshop 7 (available on the Moodle). Additionally, you can find information about the graphics package at: h​ttp://mcsp.wartburg.edu/zelle/python/graphics/graphics/index.html

Additionally, there is a population datafile from the US census that you can download from Moodle. The data file is contained in Workshop9.zip. The data file is called “CensusData2014”. It contains the official US government estimated population for every city/town in the United States with at least 50,000 people. (You should remember this file from Workshop 2.)

For this assignment, I would appreciate it if you would orient your graphics window so that Y­values increase as you go "Up" towards the top of the window. (By default the Zelle graphics package is set up so that the highest Y­values are at the bottom of the window.) This code will create a graphics window that is oriented so that Y­values increase as you approach the top of the window.

from graphics import *
width = 500
height = 400
title = ‘Graphics Window’
win = GraphWin(title, width, height)
win.setCoords(0,0,width,height)
Please feel free to change the w​idth a​nd h​eight v​alues to make the window whatever size you like.
￼￼￼
Here is function that takes in the name of a population data file and returns a list of tuples. Each tuple in the city contains a city, a state, and a population value.

def getListFromFile (filename): inputFile = open(filename) lst = []
for line in inputFile:
(city, state, population_string) = line.split(',') population = int(population_string)
tup = (city, state, population) lst.append(tup)
return lst

You should call this function and store the resulting list in a variable. You will then pass this list as an input to functions later in the workshop.
￼￼
Problem #1:
Write a function, drawRectangles, that takes a list of numbers and draws a sequence of rectangles. Each rectangle should have the same width. The height of each rectangle should be determined by the numbers in the list.
Note:​You can use whatever coordinates you want to make this look good on your screen.
For example:
drawRectangles( [200, 100, 300] )
Should draw something like this:
+­­­­+
|| +­­­­+ | | |||| | |+­­­­+| | | || || | +­­­­++­­­­++­­­­+

Problem #2:
One issue with drawRectangles is that you don't know how large the numbers will be in the list and you want the rectangles to look good regardless of how large the numbers are.
Alter drawRectangles so that the function now does the following:
● Make a copy of the list (so that you don't alter the list you are handled)
● Divide every number in the list by the maximum value in the list
● Multiple every number by a scaling factor (pick some number that work for your
window size and your screen).
While you are at it, drawRectangles might look better if you alternate colors. (This isn't required, but is something to consider.)
Note:​The scaling factor will be the height of the rectangle corresponding to the largest value in your list.

Problem #3:
Write a function, b​arChart,​that takes in a list of tuples. The first item in each tuple should be a string, the second item in each tuple should be a number.
The function b​arChart​should make rectangles whose heights are based on the numbers in the list. Use the same scaling technique from Problem 2. (You might use drawRectangles,​or you can create an altered version of d​rawRectangles i​f that makes things easier.)
Additionally, b​arChart​should label each rectangle (perhaps underneath the rectangle) with the corresponding string.
To do the labeling you will need to create T​ext o​bjects. Here is the documentation page for the T​ext o​bjects in the Zelle graphics package: http://mcsp.wartburg.edu/zelle/python/graphics/graphics/node10.html
You can test your code by running:
list1 = [ ("alice", 3), ("bob", 1), ("eve", 2) ]
￼
Problem #4:
Write a function s​umState​that takes two inputs. The first input is a list of tuples where the first item in each tuple is a city name, the second item in each tuple is a state name and the third item in each tuple is a population number. (That is, the first input is the type of list that is returned by def g​etListFromFile.​) The second input should be a state name.
The function s​umState​should return the total population of all cities in the given state.
Use s​umState​and b​arChart t​o create a chart that compares the urban populations of New York, Texas, Florida and California. (By urban, I mean people living in cities of at least 50,000 people ­­ that is, people living in cities listed in the census file.)

Problem #5:​
Write a function N​thLargestCity​that takes three inputs.The first input is a list of tuples where the first item in each tuple is a city name, the second item in each tuple is a state name and the third item in each tuple is a population number. (That is, the first input is the type of list that is returned by def g​etListFromFile.​) The second input should be the name of a state. The third input should be an integer N.
The function N​thLargestCity s​hould return a tuple. The first item in the tuple should be the name of the N​largest city in the given state. The second item in the tuple should be the population of the city. (When I say the N­th largest city, I mean that the city such that there are exactly (N­1) cities larger than the given city. For example, the 1­th largest city would be the largest city in the state and the 2­th largest city would be the next (second) largest city and so on.)
Use the functions N​thLargestCity​and b​arChart t​o create a chart that compares the populations of the 5 largest cities in Florida.