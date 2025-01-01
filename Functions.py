def printme (str):
    print(str)
    return
printme("These is the first call to the user defined fiunction!")
printme("Again second call to the same function!")
#Parameter passing
def changeme (myList):
    myList = [1,2,3,4,5]
    print(id(myList))
    print("Vaalues inside the function before change", myList)
    myList[2]=50
    print("Values inside the function after change", myList)
    return
#Now you can call change function
myList = [10,20,30]
print(id(myList))
changeme(myList)
print("Values outside the function :", myList)
#Required arguments
def printMe (str):
    print(str)
    return
printme("I am a Python programmer.")
#Keyword Arguments
def printinfo (name,age):
    print("Name: ", name)
    print("Age: ", age)
    return
printinfo("xyz", 20)
printinfo(age = 50, name = "Miki")
#Default argeuments
def printInfor(name,age=35):
    print("Name :", name)
    print("Age :", age)
    return
printInfor("xyz")
printInfor(age =50, name = "TakeOff YRN")
#Anonymous Functions "Lambda keyword is used"
multiplication = lambda num1, num2: num1 * num2
sum = lambda arg1, arg2: arg1 + arg2
print("Value of total :", sum(10,20))
print("Value of total :", sum(20,20))
print("Value of Multiplication is :", multiplication(5,10))
print("Value of multiplication is :",multiplication(12,12))
#The return Statement
def add (arg1,arg2):
    total = arg1 + arg2
    print("Insid the function :", total)
    return total
total = add(12,54)
print("Outside the function :", total)
#Scope of variables ie Global variable,local variable
total = 0
def summation(arg01 , arg02):
    total = arg01 + arg02;
    print("Inside the function loacal total :", total)
    return total
summation(34,79)
print("Outside the function global total :", total)
