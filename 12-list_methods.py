import copy

myList = [1, 2, 3, ['a', 'b', 'c']]

myList2 = ['d', 'e', 'f']

myList2.append(myList)

print(myList2)

myList3 = copy.deepcopy(myList)

print("my list id", id(myList), myList)
print("my list id", id(myList3), myList3)