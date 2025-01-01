#Choice(seq),random(),seed([x]),shufle(ist),uniform(x,y)
import random
#choice () function
print("Random number from range(100) :", random.choice(range(100)))
List = [1, 2, 3, 5, 9]
print("Random element from list :", random.choice(List))
str = "Hello World!"
print("random character from string :", random.choice(str))

#randrange () function
print("randrange(1,100,2) :", random.randrange(1, 100,2))
print("randarange(100) :", random.randrange(100))

#random() function
print("random() :", random.random())

#seed() function
random.seed()
print("random number with default seed:", random.random())

#shuffle() function
List = [1, 2, 3, 5, 9]
random.shuffle(List)
print("List after shuffling :", List)

#uniform() function
print("Random number between 1 and 10 :", random.uniform(1, 10))