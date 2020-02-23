
import random
import sys
import os

First_List = ["Aleem", "Raheem", "Saleem"]
Another_List = ["Hafeez", "Aziz"]
Lists_Together = First_List + Another_List
Lists_Together.append("Rukhsana_Malik")
print(Lists_Together)
Lists_Together.insert(2, "Tariq")
print("Maximum value is :", max(Lists_Together))
print("Minimum value is :", min(Lists_Together))
Lists_Together.append("Rabeea Anjum")
print(Lists_Together, "\nAnd the Length is : ", len(Lists_Together))

# and other methods for Lists are append(),insert(),remove(),sort(),reverse(),len(),max()
# and use del

# Data types in Python are Lists,Dictionaries,Tuples,Numbers and Strings
# Working with tuples

pi_tuple = (1,2,3,4,5,6)
print("This is a tuple ", pi_tuple)
'''
# Converting Tuple to Lists

new_list = list(pi_tuple)
print("This is a list :", new_list)
print("Length of a tuple is : ", len(pi_tuple), "\n", "Maximum value is:", max(pi_tuple),
      "\nMinimum value is : ", min(pi_tuple))
      # We can also use methods len(),max() and min() with tuples 

# --------Dictionaries------
# Note : we can not use + with dictionaries like we use in Lists
# methods for Dictionaries are get(),values(),len(),del etc

First_Man = {
    'First_Name':'Aleem',
    'Last_Name': 'Awan ',
    'Age': 2,
    'Class_Values': {
        'Session':'16-20',
        'Roll_Number':'BCSF16E007'
    }

}

print("Length of dictionary 'First Man' is : ", len(First_Man))
print(First_Man.values())
print(First_Man.keys())
print("%s %s %s %s %s" % ("First Man ", First_Man['First_Name'], First_Man['Last_Name'],First_Man['Age'] ,First_Man['Class_Values']))
del First_Man['Age']
print(First_Man['Class_Values'])'''

# -------- Conditional Statements ----------Loops --------Functions
# These includes if elif else Logical operators are 'and' , 'or' ,'not'
def Show_Name() :
    print("My name is aleem")
    new_tuple = (1,2,3,4,5,6)
    for x in new_tuple :
        if x % 2 == 0 :
            continue
        print(x)
Show_Name()

# Function with Arguments
def Print_Student(Number_List):
    marks = 0.0
    total_length = len(Number_List)
    for number2 in Number_List :
        marks = marks + number2
    number = marks / total_length
    if (number <= 100) and (number >= 85):
        print("You Got 4.00 GPA !!! Well done ")
    elif (number < 85) and (number >= 50):
        print("Your are a Student of Average GPA")
    elif (number < 0) or (number > 100):
        print("You have entered wrong marks")
    else :
        print("You need to  work hard to get success")
Number_Lists = [0,0,0,-3,0]
Print_Student(Number_Lists) 

count = 10
while count >= 0:
    if count == 3:
        count = count - 1
        continue
    elif count == 1:
        break
    print(count , " ", end="")

    count = count - 1
num_List = [[20,30,40],[50,60,70],[80,90,100]]
for index in range(0,3):
    for number in range(0,3):
        print(num_List[index][number]) 
print("what is your name")
name = sys.stdin.readline()
print("Hi ",name)
# Strings use methods replace(),strip(),split(),len(),find(),capitalize(),isalpha(),isalnum()
long_string = "My name is aleem and I like to write programs in Python"
print(len(long_string))
print(long_string.capitalize())
print(long_string.find("Python"))
print(long_string.split(" "))
print(long_string.strip())
print(long_string.isalnum())
print(long_string.isalpha())
print(long_string[-7:]) 

# ----------------------Files-----------
myFile = open("newFile.txt","wb")
print(myFile.mode)
print(myFile.name)
myFile.write(bytes("My name is aleem \n","UTF-8"))
myFile.close()

myFileForPrint = open("newFile.txt","r+")
myFileToPrint = myFileForPrint.read()
print(myFileToPrint)
myFileForPrint.close()
os.remove("newFile.txt") 
class Animal:
    __name = None
    __height = None
    __weight = None
    __sound = None

    def __init__(self,name,height,weight,sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def get_name(self):
        return self.__name
    def get_height(self):
        return self.__height
    def get_weight(self):
        return self.__weight
    def get_sound(self):
        return self.__sound
    def toString(self):
        return "{} is {} cm tall its weight is {} kilograms and sound is {}".\
            format(self.__name, self.__height,self.__weight,self.__sound)

class Dog(Animal):
    __ownerName = None
    def __init__(self,name,height,weight,sound,owner):
        self.__ownerName = owner
        super(Dog, self).__init__(name,height,weight,sound)

    def toString(self):
        return "{} is {} cm tall its weight is {} kilograms its sound is {} and its owner name is {}".\
                format(self.__name, self.__height,self.__weight,self.__sound,self.__ownerName)
myObj = Animal('Motii',45,55,'Ruff')
print(myObj.toString)
myObj2 = Dog('bhola',55,45,'Ruff','Ruby')
print(myObj2.toString)


