#Arithmetic Operators
#Comparison Operators
#Logical Operators
#Bitwise Operators
#Assignment Operators
#Special Operators
#Membership Operators
#Identity Operators

#Arithmetic Operators
a = 10
b = 20
c = 30
print("a + b = ", a+b) #Addition
print("a - b = ", a-b) #Subtraction
print("a * b = ", a*b) #Multiplication
print("a / b = ", a/b) #Float Division
print("a // b = ", a//b) #Floor Division
print("a % b = ", a%b) #Modulus Operator
print("a ** b = ", a**b) #Exponentiation Operator

#Comparison Operators
a = 10
b = 20
print("a == b = ", a==b) #Equality Operator
print("a != b = ", a!=b) #Inequality Operator
print("a > b = ", a>b) #Greater Than Operator
print("a < b = ", a<b) #Less Than Operator
print("a >= b = ", a>=b) #Greater Than or Equal To Operator
print("a <= b = ", a<=b) #Less Than or Equal To Operator

#Logical Operators
a = 10
b = 20
print("a and b = ", a and b) #Logical AND
print("a or b = ", a or b) #Logical OR
print("not a = ", not a) #Logical NOT
print("not b = ", not b) #Logical NOT

#Bitwise Operators
a = 10
b = 20
print("a & b = ", a & b) #Bitwise AND
print("a | b = ", a | b) #Bitwise OR
print("a ^ b = ", a ^ b) #Bitwise XOR
print("a << b = ", a << b) #Bitwise Left Shift
print("a >> b = ", a >> b) #Bitwise Right Shift

#Assignment Operators
a = 10
b = 20
a += b
print("a += b = ", a)
a -= b
print("a -= b = ", a)
a *= b
print("a *= b = ", a)
a /= b
print("a /= b = ", a)
a %= b
print("a %= b = ", a)
a //= b
print("a //= b = ", a)
a **= b
print("a **= b = ", a)

#Special Operators
a = 10
b = 20
print("a is b = ", a is b)
print("a is not b = ", a is not b)

#Membership Operators
x = 10
y = 20
list = [1, 2, 3, 4, 5]
print(list)
print("x= ", x, "y= ", y)
if (x in list):
    print("x is available in the list")
else:
    print("x is not available in the list")

if (y not in list):
    print("y is not available in the list")
else:
    print("y is available in the list")
c = 2
print("c-",c )
if c in list:
    print("c is available in the list")
else:
    print("c is not available in the list")

#Identity Operators - compares memory location of two objects
a = 10
b = 20
print("a is b = ", a is b)
print("a is not b = ", a is not b)