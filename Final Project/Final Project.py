# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 19:25:39 2021

@author: Mehmet Can Yıldırım
"""
points = [] # Creation of the empty list for points.

print("Welcome the knowledge competition!") 

q1 = input("Q1) What is the capital of Turkey?\n Your answer is: ") # First question of the competition.
if q1.capitalize() == "Ankara":                                     # Standardization of the written answer.
    print("Correct Answer. Congurats! You got 10 points.")
    points.append(10)                                               # Adding 10 points to the list.
else:
    print("Wrong Answer, it is Ankara.")
    
q2 = input("Q2) Which Turkish team did Alex De Souza play in?\n Your answer is: ") # Second question of the competition.
if q2.capitalize() == "Fenerbahce" or q2.capitalize == "Fenerbahçe":               # Standardization of the written answer.
    print("Correct Answer. Congurats! You got 10 points.")
    points.append(10)                                                              # Adding 10 points to the list.
else:
    print("Wrong Answer, it is Fenerbahce.")

q3 = input("Q3) How many months are there in a year?\n Your answer is: ") # Third question of the competition.
if q3.capitalize() == "twelve" or q3 == "12":                             # Standardization of the written answer.
    print("Correct Answer. Congurats! You got 10 points.")
    points.append(10)                                                     # Adding 10 points to the list.
else:
    print("Wrong Answer, it is twelve(12).")  
    
q4 = input("Q4) How many valves are there in a heart?\n Your answer is: ") # Fourth question of the competition.
if q4.capitalize() == "four" or q4 == "4":                                 # Standardization of the written answer.
    print("Correct Answer. Congurats! You got 10 points.")
    points.append(10)                                                      # Adding 10 points to the list.
else:
    print("Wrong Answer, it is four(4).")

q5 = input("Q5) What is the most crowded country in the world?\n Your answer is: ") # Fifth question of the competition.
if q5.capitalize() == "China":                                                      # Standardization of the written answer.
    print("Correct Answer. Congurats! You got 10 points.")
    points.append(10)                                                               # Adding 10 points to the list.
else:
    print("Wrong Answer, it is China.")
    
q6 = input("Q6) What is the most spoken language in the world?\n Your answer is: ") # Sixth question of the competition.
if q6.capitalize() == "Chinese":                                                    # Standardization of the written answer.
    print("Correct Answer. Congurats! You got 10 points.")
    points.append(10)                                                               # Adding 10 points to the list.
else:
    print("Wrong Answer, it is Chinese.")
    
q7 = input("Q7) What is the satellite of our world?\n Your answer is: ") # Seventh question of the competition.
if q7.capitalize() == "Moon":                                            # Standardization of the written answer.
    print("Correct Answer. Congurats! You got 10 points.")
    points.append(10)                                                    # Adding 10 points to the list.
else:
    print("Wrong Answer, it is Moon.")
 
q8 = input("Q8) How many days are there in June?\n Your answer is: ") # Eighth question of the competition.
if q8.capitalize() == "thirty" or q8 == "30":                         # Standardization of the written answer.
    print("Correct Answer. Congurats! You got 10 points.")
    points.append(10)                                                 # Adding 10 points to the list.                        
else:
    print("Wrong Answer, it is Thirty(30).")
    
q9 = input("Q9) What is the most crowded city in the Turkey?\n Your answer is: ") # Ninth question of the competition.
if q9.capitalize() == "Istanbul" or q9.capitalize() == "İstanbul":                # Standardization of the written answer.  
    print("Correct Answer. Congurats! You got 10 points.")
    points.append(10)                                                             # Adding 10 points to the list.                  
else:
    print("Wrong Answer, it is Istanbul.")
    
q10 = input("Q10) What is the most crowded city in the world?\n Your answer is: ") # Tenth question of the competition.
if q10.capitalize() == "Tokyo":                                                    # Standardization of the written answer.                             
    print("Correct Answer. Congurats! You got 10 points.")
    points.append(10)                                                              # Adding 10 points to the list.         
else:
    print("Wrong Answer, it is Tokyo.")
   
points = sum(points)                                                               # Summation of the all points.
print("\nThe competition is over.")
print("Total score is: " + str(points))                                                

# Determination of the successful or unsuccessful of the competitor.
if points > 50:                                                                    
    print("Well done, you're successful!")
elif points <= 50:
    print("Sorry, you're not successful!")
    
    
    