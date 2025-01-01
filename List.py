mylist1 = ['Phydsics', 'Chemistry', 1997, 2000]
mylist2 = [1, 2, 3, 4, 5]
mylist3 = ["a", "b", "c", "d"]
print("list1[0]: ", mylist1[0])
print("list2[1:5]: ", mylist2[1:5])
print("list3[0:3]: ", mylist3[0:3])
print(mylist2)
print(mylist3)

#Updating list
mylist1[0] = 'Maths'
print(mylist1)

#Deleting list
del mylist1[0]
print(mylist1)

#Length of list
print(len(mylist1))
print(mylist1)
#Basic list operations
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print(list, tinylist)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist * 2)
print(list + tinylist)

#Indexing,slicing and matrix
L = ['spam', 'Spam', 'SPAM!']
print(L[2])
print(L[-2])
print(L[1:])
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][1])

#List build in Functions
#len() function
list1 = ['Physics', 'Chemistry', 'Maths']
print(list1)
list2 = list(range(5))
print(list2)
print("length = ",len(list2))

#max() function
list1, list2 = ['C++', 'Java', 'Python'], [456, 700,200]
print(list1, list2)
print("Max value element :", max(list1))
print("Max value element :", max(list2))

#Min() function
print("Min value elment :", min(list1))
print("Min value element :", min(list2))

#list() function
aTuple = (123, 'C++', 'Java', 'Python')
list1 = list(aTuple)
print("List of elements :", list2)

str = "hello World"
list2 = list(str)
print("Last Elements :", list2)