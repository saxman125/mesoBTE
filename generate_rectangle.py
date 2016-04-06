import numpy as np
import pylab
import math

f =open("rectangle.txt", "w")

number_holes = input("Please input the number of holes: ")
vertex_number = []
vertex_x = []
vertex_y = []
length_x=[]
length_y= []
inside_x =[]
inside_y = []
edges = []
edge1 = []
edge2 = []

for i in range(1,number_holes+1):
    vertex_number.append(i)
    vertex_number.append(i)
    vertex_number.append(i)
    vertex_number.append(i)

    edges.append(i)
    edges.append(i)
    edges.append(i)
    edges.append(i)

if number_holes == 1:
        count =1
else:
        count= number_holes-1
for i in range(0,count):
    #get length in x and y directions of hole
    temp_xlen = input("Please input the width in x of hole.")
    length_x.append(temp_xlen)

    temp_ylen = input("Please input the height in y of hole.")
    length_y.append(temp_ylen)

    #get coordinates of bottom left vertex of hole. then calculate vertices as follows:
    # bottom left, bottom right, top right, top left
    temp_xcent = input("Please input the x coordinate of bottom left vertex of hole.")
    vertex_x.append(temp_xcent)
    vertex_x.append(temp_xcent + temp_xlen)
    vertex_x.append(temp_xcent + temp_xlen)
    vertex_x.append(temp_xcent)
    
    temp_ycent = input("Please input the y coordinate of bottom left vertex of hole.")
    vertex_y.append(temp_ycent)
    vertex_y.append(temp_ycent)
    vertex_y.append(temp_ycent+ temp_ylen)
    vertex_y.append(temp_ycent+ temp_ylen)

    #get edges and define boundaries using vertices above
    edge1.append(vertex_number[i+3])
    edge2.append(vertex_number[i])

    edge1.append(vertex_number[i])
    edge2.append(vertex_number[i+1])

    edge1.append(vertex_number[i+1])
    edge2.append(vertex_number[i+2])

    edge1.append(vertex_number[i+2])
    edge2.append(vertex_number[i+3])
    
    #get coordinates of point inside hole
    temp_xin = input("Please input the x coordinate of a point inside hole.")
    inside_x.append(temp_xin)

    temp_yin = input("Please input the y coordinate of a point inside hole.")
    inside_y.append(temp_yin)

#add vertices and edges for main grid
vertex_x.append(0)
vertex_x.append(1)
vertex_x.append(1)
vertex_x.append(0)

vertex_y.append(0)
vertex_y.append(0)
vertex_y.append(1)
vertex_y.append(1)

#bottom left
edge1.append(vertex_number[number_holes*4+3])
edge2.append(vertex_number[number_holes*4])

#bottom right
edge1.append(vertex_number[number_holes*4])
edge2.append(vertex_number[number_holes*4+1])

#top right
edge1.append(vertex_number[number_holes*4+1])
edge2.append(vertex_number[number_holes*4+2])

#top left
edge1.append(vertex_number[number_holes*4+2])
edge2.append(vertex_number[number_holes*4+3])

#intro line
f.write(str(4*number_holes +4) + " 2 0 1 \n")

#vertices
for j in range(0,4*number_holes + 3):
    f.write(str(vertex_num[j]) + " " + str(vertex_x[j]) + " " + str(vertex_y[j]) + " \n")

#edges
f.write(str(4*number_holes +3) + " 0 \n")

for j in range(0,4*number_holes + 3):
    f.write(str(edge[j]) + " " + str(edge1[j]) + " " + str(edge2[j]) + " \n")


#holes
f.write(str(number_holes) + "\n")
for j in range(0,number_holes-1):
    f.write(str(edge[j]) + " " + str(edge1[j]) + " " + str(edge2[j]) + " \n")






    

