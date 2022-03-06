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
   
print(my_func(0.1,0.1,0.1))

#Q2

import math  #Method modf() returns the fractional and integer parts of x in a two-item tuple
def  convert(hours, minutes):
    if type(hours)==float or type(hours)==int and type(minutes)==float or type(hours)==int and hours > 0  and minutes > 0 :
        split_h= math.modf(hours) #Split the number for two float numbers (first= minutes, second= hours)
        num_minutes= split_h[0]
        num_hours= split_h[1]
        sec_minutes= num_minutes*3600 #Turning minutes into seconds (multipying by 60*60 because we get a Decimal number)
        sec_hours= num_hours*3600 #Turning hours into seconds
        sec_minutes1=minutes*60 #Turning minutes into seconds
        sum_seconds= sec_minutes+sec_hours+sec_minutes1
        return sum_seconds
    else:
        print("Input error!")
print(convert(4.5896, 44.2))