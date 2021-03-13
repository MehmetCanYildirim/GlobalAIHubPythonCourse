# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 11:21:34 2021

@author: Mehmet Can Yıldırım
"""

list1 = list(range(9,18,2)) # Creation a list with odd numbers.
list2 = list(range(10,19,2)) # Creation a list with even numbers.

print(list1)  # To see list1 values, we can use the print function.
print(list2)  # To see list2 values, we can use the print function.

list3 = list1 + list2 # Merging the list each other.
print(list3) # Printing the merged list.

list4 = [] # Creation of the empty list.
for i in list3: # Using "for" loop to multiply by 2 each values of the list.  
   i = i * 2
   list4.append(i)
print(list4) # Printing the the values in the list multiplied by 2.
    

for j in list4: # Using "for" loop to show the type of the values of the list.
    j =+ 1
    print(type(j))
    
