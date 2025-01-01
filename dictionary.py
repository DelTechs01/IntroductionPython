dict = {'Name': 'Bleah', 'Age' : 22, 'Class': 'First'}
print(dict)
print("dict['Name'] :",dict['Name'])
print("dict['Age'] :", dict['Age'])
input()
print("Update Dictionary")
dict['Age'] = 8
dict['School'] = "Kirinyaga University"
print("dict['Age'] : ", dict['Age'])
print("dict['School'] :", dict['School'])
print("After update : ", dict)
input()
#Delete
print("Deleting from dictionary")
dict = {'Name':'Zara','Age': 7,'Class': 'First'}
print("Initial dictionary", dict)
del dict['Name']
print("Dictionary after removing element :",dict)
dict.clear()
print("Dictionary after clear", dict)
del dict

print("dict['Age'] :", dict['Age'])
print("dict['School'] :", dict['School'])

dict.get()
dict = dict.fromkeys(10)
dict.items()
dict1 = dict.copy()
dict.keys()
dict.values()
dict.setdefaults()
dict.update()