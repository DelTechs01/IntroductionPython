mystr1 = "Welcome"
mystr2 = "to Python"

print(mystr1 + " " + mystr2)

str = "Hello World!"
print(str)
print(str[0])
print(str[2:5])
print(str[2:])
print(str * 2)
print(str + "TEST")

#using string formating operators
name = 'xyz'
print('Hello, %s!' % name)
print('Hello, {}!'.format(name))
marks = 80
print('Hello, {name}! Your marks is {marks}'.format(name=name, marks=marks))
print('Hello, {0}! Your marks is {1}'.format(name, marks))
print("Marks in octal %o", marks)
print("Marks in hex %x", marks)

#using string methods
str = "Hello, World!"
print(str.upper())
print(str.lower())
print(str.strip())
print(str.split(","))
print(str.replace("H", "J"))
print(str.find("o"))

#triple quotes
str = '''These is the long string that is made up
of multiple lines and non-printable characters such as (\t) and 
they will show up that way when displayed.NEWLINEs within the string, whether explictly
given like thi within the brackets[\n], or just a NEWLINE within the variable
assignment will also show up.'''
print(str)
print('C:\\demo')
print(r'C:\\demo')

#String encoding Functions
import base64
str = "this string is example.....wow!!"
str = base64.b64encode(str.encode("ascii"))
print("Encode string: ", str)
str = base64.b64decode(str).decode("ascii")
print("Decode string: ", str)