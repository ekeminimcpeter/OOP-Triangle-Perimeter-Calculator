#Author: Ekemini Peter [McPeter McPeter]
#Description: A program that calculates the perimeter of a triangle described by three points
#Date:29/05/2025
#Revision: Rev 0
'''
Now we're going to embed the Point class (see Lab 3.4.1.14) inside another class. Also, we're going to put three points into one class, which will let us define a triangle. How can we do it?

The new class will be called Triangle and this is what we want:

the constructor accepts three arguments – all of them are objects of the Point class;
the points are stored inside the object as a private list;
the class provides a parameterless method called perimeter(), which calculates the perimeter of the triangle described by the three points; the perimeter is the sum of all the lengths of the legs (we mention this for the record, although we are sure that you know it perfectly yourself.)
Complete the template we've provided in the editor. Run your code and check whether the evaluated perimeter is the same as ours.

Below you can copy the Point class code we used in the previous lab:

Check ***

Expected output

3.414213562373095

'''

import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(abs(self.__x - x), abs(self.__y - y))

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1,vertice2,vertice3] # points are stored inside the object as a private list
       

    def perimeter(self):
        length_side_1 = self.__vertices[0].distance_from_point(self.__vertices[1]) #calculate length of first side of triangle from the distance between boundarying vertice 1 & 2
        length_side_2 = self.__vertices[1].distance_from_point(self.__vertices[2]) #calculate length of second side of triangle from the distance between boundarying vertice 2 & 3
        length_side_3 = self.__vertices[2].distance_from_point(self.__vertices[0]) #calculate length of third side of triangle from the distance between boundarying vertice 3 & 1
        self.__perimeter_of_triangle = length_side_1 + length_side_2 + length_side_3 #Sum of lengths of sides of triangles
        return self.__perimeter_of_triangle
        

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
#triangle = Triangle(Point(4, 20), Point(5, 10), Point(8, 16))
print(triangle.perimeter())
    
