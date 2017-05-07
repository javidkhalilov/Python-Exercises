# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 10:59:45 2016

@author: Javid
"""

import turtle


def open_window():
    window=turtle.Screen()
    window.bgcolor("red")
    window.exitonclick()
    
def draw_square():
    i=0

    
    brad=turtle.Turtle()
    brad.color("yellow")
    brad.shape("turtle")
    brad.speed(2)
    
    while(i<4):
        brad.forward(100)
        brad.right(90)
        i=i+1
      
def draw_circle():
    angie=turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    
#def draw_triangle():
#    eda=turtle.Turtle()
#    eda.shape("turtle")
#    eda.color("green")
#    
#    for j in range(1,4):
#        eda.right(60)
#        eda.forward(100)

open_window()  
draw_square()
draw_circle()
#draw_triangle()
