"""
Name:           Aiman Haroon
Course:         Cis 2531 Net01
Professor:      Shamsuddin, Sheikh
Program:        Final Project
Description:    this program has 3 classes: circle, square, and cube that inherits an abstract
                class Geometry. Each class has getters, setters, find_area method, and display
                The purpose of the program to print the area and display function of any class
                depending on the value of the random number generator. finally, the program
                shows output in 3 ways: screen, file, and Gui window.
"""


import random
import math
from tkinter import *

#abstract class
from abc import ABC, abstractmethod
 
class Geometry(ABC):
 
    @abstractmethod
    def __init__(self):
        pass

#class #1
class Circle(Geometry):

    #constructor
    def __init__(self, radius = 5):
        self.__radius = radius

    #accessor
    def get_radius(self):
        return (self.__radius)

    #mutator
    def set_radius(self, radius):
        self.__radius = radius

    #method for find area of the shape
    def find_area(self):
        return (self.__radius * self.__radius) * math.pi

    #method to display the class name and its attributes
    def display(self):
        return (obj.__dict__)#returns the name and attribute of the class with attribute default value


#class #2        
class Square(Geometry):
    
    #constructor
    def __init__(self, side = 5.3):
        self.__side = side

    #accessor
    def get_side(self):
        return (self.__side)

    #mutator
    def set_side(self, side):
        self.__side = side

    #method for find area of the shape
    def find_area(self):
        return(self.__side * self.__side) 

    #method to display the class name and its attributes
    def display(self):
        return (Square.__name__, obj.__dict__)#returns the name and attribute of the class with attribute default value

#class #3
class Cube(Geometry):
    #constructor
    def __init__(self, length = 2.5):
        self.__length = length

    #accessor
    def get_length(self):
        return (self.__length)

    #mutator
    def set_length(self, length):
        self.__length = length

    #method for find area of the shape
    def find_area(self):
        return (6 * (self.__length * self.__length) )

    #method to display the class name and its attributes
    def display(self):
        return (Cube.__name__, obj.__dict__)#returns the name and attribute of the class with attribute default value




#main program starts here..




#ask user to enter the name of the file
file_name = input("Enter the name of the file to save the program output: ")




#generating random number to decide which class objects to display first
opt = random.randint(1,3)  #generating number between 1 - 3



#if random no is 1, prints class Circle

if opt == 1:
    print("\nThe random number is ", opt)
    print("Printing Circle objects with default constructor\n")
    circle_list = []      #making a list to store objects values
    for i in range(10):    
        obj = Circle()
        circle_list.append(obj)

    #print the result on Gui Window
    win_circle = Tk()
    win_circle.title("Areas of Geometry Shapes")
    win_circle.geometry("400x200")

    main_label = Label(win_circle, text="Area of Circle")
    main_label.grid(column=1, row=0)

    constr = Label(win_circle, text="Using default constructor").grid(column=1, row=1)

    current_class = Label(win_circle, text="Class Name: ").grid(column=0, row=2)
    class_name = Label(win_circle, text="Circle").grid(column=1, row=2)
                                                   
    class_attribute = Label(win_circle, text="Attributes: ").grid(column=0, row=3)
    attribute_name = Label(win_circle, text="Radius: 5cm").grid(column=1, row=3)

    area = Label(win_circle, text="Area: ").grid(column=0, row=4)


    #print the results on screen and add area value to Gui 
    for i in circle_list:
       
        print(i.display())
        print(i.find_area())
        value = (i.find_area())
        area_value = Label(win_circle, text=value).grid(column=1, row=4)

    #print the results on the file
    file = open(file_name+".txt", "w")
    file.write("The random number is " + str(opt))
    file.write("\nPrinting Circle objects with default constructor\n")
    file.write("\n")
    for k in circle_list:
        file.write(str(i.display()))
        file.write("\n")
        file.write(str(i.find_area()))
        file.write("\n")

    file.close()


#if random no is 2, prints class Square    

elif opt == 2:
    print("\nThe random number is ", opt)
    print("Printing Square objects with default constructor\n")
    square_list = []   #making a list to store objects values
    for i in range(10):
        obj = Square()
        square_list.append(obj)

    #print the result on Gui Window
    win_square = Tk()
    win_square.title("Areas of Geometry Shapes")
    win_square.geometry("400x200")

    main_label = Label(win_square, text="Area of Square")
    main_label.grid(column=1, row=0)

    constr = Label(win_square, text="Using default constructor").grid(column=1, row=1)

    current_class = Label(win_square, text="Class Name: ").grid(column=0, row=2)
    class_name = Label(win_square, text="Square").grid(column=1, row=2)
                                                   
    class_attribute = Label(win_square, text="Attributes: ").grid(column=0, row=3)
    attribute_name = Label(win_square, text="Side: 5.3cm").grid(column=1, row=3)

    area = Label(win_square, text="Area: ").grid(column=0, row=4)

    #print the result on screen and add area value to Gui 
    for i in square_list:       
        print(i.display())
        print(i.find_area())
        value = (i.find_area())
        area_value = Label(win_square, text=value).grid(column=1, row=4)

    #print the results on the file
    file = open(file_name+".txt", "w")
    file.write("The random number is " + str(opt))
    file.write("\nPrinting Square objects with default constructor\n")
    file.write("\n")
    for k in square_list:
        file.write(str(i.display()))
        file.write("\n")
        file.write(str(i.find_area()))
        file.write("\n")

    file.close()




#if random no is 3, prints class Cube    

else:
    print("\nThe random number is ", opt)
    print("Printing Cube objects with default constructor\n")
    cube_list = []    #making a list to store objects values
    for i in range(10):
        obj = Cube()
        cube_list.append(obj)

    #print the result on Gui Window
    win_cube = Tk()
    win_cube.title("Areas of Geometry Shapes")
    win_cube.geometry("400x200")

    main_label = Label(win_cube, text="Area of Cube")
    main_label.grid(column=1, row=0)

    constr = Label(win_cube, text="Using default constructor").grid(column=1, row=1)

    current_class = Label(win_cube, text="Class Name: ").grid(column=0, row=2)
    class_name = Label(win_cube, text="Cube").grid(column=1, row=2)
                                                   
    class_attribute = Label(win_cube, text="Attributes: ").grid(column=0, row=3)
    attribute_name = Label(win_cube, text="length: 2.5cm").grid(column=1, row=3)

    area = Label(win_cube, text="Area: ").grid(column=0, row=4)


    #print the result on screen and add area value to Gui 
    for i in cube_list:
        print(i.display())
        print(i.find_area())
        value = (i.find_area())
        area_value = Label(win_cube, text=value).grid(column=1, row=4)

    #print the results on the file
    file = open(file_name+".txt", "w")
    file.write("The random number is " + str(opt))
    file.write("\nPrinting Cube objects with default constructor\n")
    file.write("\n")
    for k in cube_list:
        file.write(str(i.display()))
        file.write("\n")
        file.write(str(i.find_area()))
        file.write("\n")

    file.close()




