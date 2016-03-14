#This program will generate random points and use probability 
#   in order to calculate the value of PI

#Vikram Anjur
#03.08.2016

#import important libraries/functions for later use in this program
from __future__ import division
import random
import matplotlib.pyplot as plt
import pylab
import numpy 

#define some important global variables
a=1                 #used as paramater to break while loop
numcount=0          #keeps track of number of iterations we have
incount=0           #keeps track of number of random points generated within function
outcount=0          #keeps track of number of random points generated outside of function
topcount = 3000     #the maximum number of allowed iterations. 
x_list=[]           #list of the x-coordinates of randomly generated points
y_list=[]           #list of the y-coordinates of randomly generated points

# Begin to compose plot of quarter unit circle
z = numpy.linspace(0,1,100) # 100 linearly spaced numbers
t = numpy.sqrt(1-z*z) # computing the values of y along the quarter unit circle 


while(a==1):
    numcount+=1     #increment the iteration count
    
    #generate random float between [0,1)
    x=random.random()
    y=random.random()
    
    #add the randomly generated coordinates to their respective arrays
    x_list.append(x)
    y_list.append(y)
    
    #check if point (x,y) lies on or within quarter circle in first quadrant
    if(x*x + y*y <=1):
        incount +=1     #if so, increment incount
    else:
        outcount+=1     #incrememnt outcount
    
    
    #check to see if we can achieve 4 decimals of accuracy before the maximum 
    #   number of allowed iterations
    if(4*incount/(incount+outcount) == 3.1415):
        print "The value of PI is %f" % (4*incount/(incount+outcount)) #area of quarter unit circle = PI/4
        print "The number of points within or on the quarter circle was: %d" % incount
        print "The number of points outside the quarter circle was: %d" % outcount
        print "The total number of iterations to achieve this accuracy was: %d" % numcount        

        pylab.scatter(x_list,y_list) #add all the individual, randomly generated points (blue)
        pylab.plot(z,t,'r') #plot the quarter unit circle in red
        pylab.show() # show the plot
        a=0 #break while loop
        
    #check to see if we've reached the maximum number of allowed iterations
    elif(numcount == topcount):
        print "We stopped running the program at %d iterations." %topcount
        print "The calculated value of PI is %f" % (4*incount/(incount+outcount))
        print "The number of points within or on the quarter circle was: %d" % incount
        print "The number of points outside the quarter circle was: %d" % outcount
        print "The total number of iterations to achieve this accuracy was: %d" % numcount
              
        pylab.scatter(x_list,y_list) #add all the individual, randomly generated points (blue)
        pylab.plot(z,t,'r') #plot the quarter unit circle in red
        pylab.show() # show the plot
        a=0 #break while loop
        
