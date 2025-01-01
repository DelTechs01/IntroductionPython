#methods append(), count(), extend(), index(), insert(), pop(), remove(), reverse(), sort(), clear()

#append() method
print("append() method")
list1 = ['C++', 'Java', 'Python']
list1.append('C#')
print("Update list", list1)

#count() method
print("count()  method")
aList = [123, 'xyz', 'zara', 'abc', 123];
print("Count for 123 : ", aList.count(123))
print("Count for xyz : ", aList.count('xyz'))
print("Count for zara : ", aList.count('zara'))

#extend() method
print("extend() method")
list1 = ['C++', 'Java', 'Python']
list2 = list(range(5))
print(list1, list2)
list1.extend(list2)
print("Extended List", list1)

#index() method
print("index() method")
listm = ['Physics', 'Chemistry', 1997, 2000]
print(listm)
print("Index for 1997 : ", listm.index(1997))
print("Index for 2000 : ", listm.index(2000))
print("Index of C#", list1.index)

#insert() method
print("insert() method")
list1 = ['C++', 'Java', 'Python']
list1.insert(1, 'C#')
print("Insert list", list1)

#pop() method
print("pop() method")
list1 = ['C++', 'Java', 'Python']
print("Pop List", list1)
list1.pop()
print("Pop List", list1)
list1.pop(1)
print("Pop List", list1)

#remove() method
print("remove() method")
list1 = ['C++', 'Java', 'Python']
print("Remove List", list1)
list1.remove('Java')
print("Remove List", list1)

#reverse() method
print("reverse() method")
list1 = ['C++', 'Java', 'Python']
print("Reverse List", list1)
list1.reverse()
print("Reverse List", list1)

#sort() method
print("sort() method")
list1 = ['C++', 'Java', 'Python']
print("Sort List", list1)
list1.sort()
print("Sort List", list1)

#clear() method
print("clear() method")
list1 = ['C++', 'Java', 'Python']
print("Clear List", list1)
list1.clear()
print("Clear List", list1)
