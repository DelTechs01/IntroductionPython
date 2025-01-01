tup1 = ('Physics', 'Chemistry', 1997, 200)
tup2 = (1, 2, 3, 4, 5, 6, 7)
print(tup1, tup2)
print("tuple[0]: ", tup1[0])
print("tup2: ", tup2[1:5])
input("Continue")
#updating
print("Tuple Update example")
tup1 = (12, 34.56)
tup2('abc', 'xyz')
print(tup1,tup2)
#So let's create a new tuple as follows
tup3 = tup1 + tup2
print("New tuple :", tup3)
input("Continue")
#delete
print("delete tuple example")
tup = ('Physics', 'Chemistry', 1997, 2000)
print("Before deleting: ", tup)
del tup
print("After deleting tup : ")
print(tup)

#Operations on tuple
tuple1,tuple2 = (123,'xyz', 'zara'), (456, 'abc')
print("Len Function")
print(tuple1, tuple2)

