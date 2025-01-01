tuple1,tuple2 = (123, 'xyz', 'zara'), (456, 'abc')
#len() function
print("Len function")
print(tuple1, tuple2)
print("First Tuple length : ", len(tuple1))
print("Second tuple length : ", len(tuple2))
input()
#Max() function
tuple01, tuple02 = ('maths', 'chemistry', 'Physics', 'Biology'), (456, 700, 200)
print("Max Function")
print(tuple01, tuple01)
print("Max value element in tuple01 : ", max(tuple01))
print("Max value element in tuple02 : ", max(tuple02))
input()
#Min() function
print("Min() function")
print(tuple01, tuple02)
print("Min value element in tuple01 : ", min(tuple01))
print("Min value element in tuple 01 : ", min(tuple02))

#tuple() function
list1 = ['maths', 'che', 'phy', 'bio']
print("Tuple function")
print(list1)
tuple = tuple(list1)
print("Tuple from list1 : ", tuple1)
print("Tuple from string : ", tuple('Hello'))