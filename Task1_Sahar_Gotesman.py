# -*- coding: utf-8 -*-
#Sahar Gotesman 206014300
###Task 1

#Q1


def my_func(x1,x2,x3):
    denominator= x1 + x2 + x3 #sum the numbers to make sure they are equal to zero
    if denominator == 0:
            return "Not a number - denominator equels zero"
    if (type(x1) != float):
            return "Error: parameters should be float"
    elif (type(x2) != float):
            return "Error: parameters should be float"
    elif (type(x3) != float):
            return "Error: parameters should be float"
    
    return((x1+x2+x3)*(x2+x3)*x3)/denominator
   
#print(my_func(0,1,0))# usage example

#Q2
from datetime import timedelta
import math  #Method modf() returns the fractional and integer parts of x in a two-item tuple
def  convert(hours, minutes):
    if type(hours)==float or type(hours)==int and type(minutes)==float or type(hours)==int and hours >= 0  and minutes >= 0 :
        split_h= math.modf(hours) #Split the number for two float numbers (first= minutes, second= hours)
        num_minutes= split_h[0]*60
        num_hours= split_h[1]
        td = timedelta(hours = num_hours, minutes = num_minutes+minutes)
        sum_seconds= td.seconds
        return sum_seconds
    else:
        print("Input error!")
#print(convert(1,3)) #usage example