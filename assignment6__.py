# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 13:34:20 2022

@author: Raghav
"""

#Question 1

n = int(input("Enter any number: "))
sum1 = 0
for i in range(1,n):
    if(n%i==0):
        sum1 = sum1 + i
if(sum1 == n):
    print("The number is a perfect number!")
else:
    print("The number is not a perfect number!")



#Question 2

s = input("Enter a word: ")
if s == s[::-1]:
    print("This word is a Palindrome")
else:
    print("This is not a Palindrome")



#Question 3

def pascal_triangle(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
       print(trow)
       trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1 
pascal_triangle(5)



#Question 4

def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        return False
    return True
string = 'The quick brown fox jumps over the lazy dog'
if(ispangram(string)== True):
    print("Yes")
else:
    print("No")   



#Question 5

n = input("Enter a string: ")
l = n.split("-")
l.sort()
print("-".join(l))



#Question 6

def student_data(student_id, **args):
    print(f'\nStudent ID: {student_id}')
    if 'student_name' in args:
        print(f"Student Name: {args['student_name']}")
        
    if 'student_name' and 'student_class' in args:
            print(f"\nStudent Name: {args['student_name']}")
            print(f"Student Class: {args['student_class']}")

student_data(student_id='8022', student_name='Raghav Jindal', student_class='Metallurgy')
student_data(student_id='8028', student_name='Aayush Sood', student_class='Metallurgy')            




#Question 7

class Student:
    pass 
class Marks:
    pass 
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks)) 
print(isinstance(student1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))




#Question 8

class py_solution:
 def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))
      
      

      
#Question9

class py_solution:
   def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

print(py_solution().is_valid_parenthese("(){}[]"))
print(py_solution().is_valid_parenthese("()[{)}"))
print(py_solution().is_valid_parenthese("()"))            