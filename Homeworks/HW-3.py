# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 12:41:33 2021

@author: Mehmet Can Yıldırım
"""

students = [] # Creation empty list.

student1 = input("enter the name of the first student:") # Name of the first student.
midterm1 = float(input("enter the midterm grade:")) # Midterm grade of the first student.
project1 = float(input("enter the project grade:")) # Project grade of the first student.
final1 = float(input("enter the final grade:")) # Final grade of the first student.

student2 = input("enter the name of the second student:") # Name of the second student.
midterm2 = float(input("enter the midterm grade:")) # Midterm grade of the second student.
project2 = float(input("enter the project grade:")) # Project grade of the second student.
final2 = float(input("enter the final grade:")) # Final grade of the second student.

student3 = input("enter the name of the third student:") # Name of the third student.
midterm3 = float(input("enter the midterm grade:")) # Midterm grade of the third student.
project3 = float(input("enter the project grade:")) # Project grade of the third student.
final3 = float(input("enter the final grade:")) # Final grade of the third student.

student4 = input("enter the name of the fourth student:") # Name of the fourth student.
midterm4 = float(input("enter the midterm grade:")) # Midterm grade of the fourth student.
project4 = float(input("enter the project grade:")) # Project grade of the fourth student.
final4 = float(input("enter the final grade:")) # Final grade of the fourth student.
 
student5 = input("enter the name of the fifth student:") # Name of the fifth student.
midterm5 = float(input("enter the midterm grade:")) # Midterm grade of the fifth student.
project5 = float(input("enter the project grade:")) # Project grade of the fifth student.
final5 = float(input("enter the final grade:")) # Final grade of the fifth student.

students = [student1 + "," + student2 + "," + student3 + "," + student4 + "," + student5] # Adding students to the list.
print(students)


passingGrade1 = midterm1*(0.3) + project1*(0.3) + final1*(0.4) # Calculation of the passing grade for first student
print(passingGrade1)
   
passingGrade2 = midterm2*(0.3) + project2*(0.3) + final2*(0.4) # Calculation of the passing grade for second student
print(passingGrade2)

passingGrade3 = midterm3*(0.3) + project3*(0.3) + final3*(0.4) # Calculation of the passing grade for third student
print(passingGrade3)

passingGrade4 = midterm4*(0.3) + project4*(0.3) + final4*(0.4) # Calculation of the passing grade for fourth student
print(passingGrade4)

passingGrade5 = midterm5*(0.3) + project5*(0.3) + final5*(0.4) # Calculation of the passing grade for fifth student
print(passingGrade5)

# Creation a dictionary for the first student.
ögrenci1 = {"isim": student1,               
            "midterm": midterm1,
            "project": project1,
            "final": final1,
            "passingGrade": passingGrade1
            }
print(ögrenci1)

# Creation a dictionary for the second student.
ögrenci2 = {"isim": student2, 
            "midterm": midterm2,
            "project": project2,
            "final": final2,
            "passingGrade": passingGrade2
            }
print(ögrenci2)

# Creation a dictionary for the third student.
ögrenci3 = {"isim": student3, 
            "midterm": midterm3,
            "project": project3,
            "final": final3,
            "passingGrade": passingGrade3
            }
print(ögrenci3)

# Creation a dictionary for the fourth student.
ögrenci4 = {"isim": student4, 
            "midterm": midterm4,
            "project": project4,
            "final": final4,
            "passingGrade": passingGrade4
            }
print(ögrenci4)

# Creation a dictionary for the fifth student.
ögrenci5 = {"isim": student5, 
            "midterm": midterm5,
            "project": project5,
            "final": final5,
            "passingGrade": passingGrade5
            }
print(ögrenci5)

passgrades = [passingGrade1] # Creation a list for passing grades and adding the passing grade of the first student.
passgrades.insert(1,passingGrade2) # Adding the passing grade of the second student to first student.
passgrades.insert(2,passingGrade3) # Adding the passing grade of the third student to second student.
passgrades.insert(3,passingGrade4) # Adding the passing grade of the fourth student to third student.
passgrades.insert(4,passingGrade5) # Adding the passing grade of the fifth student to fourth student.
print(passgrades)

passgrades.sort() # Sorting of the list from small to large.
print(passgrades)

passgrades.reverse() # Sorting of the list from large to small by using reverse.
print(passgrades)