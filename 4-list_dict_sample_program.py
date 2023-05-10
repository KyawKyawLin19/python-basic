myName = 'Kyaw Kyaw Lin'
age = 'twenty nine'
myageReversed = reversed(age)
for i in myageReversed:
    print(i)
myList = [10, 20, 30, 40, 50]
myReversedList = reversed(myList)

for i in myReversedList:
    print(i)
myDict = {"name" : "Kyaw Kyaw Lin", "age" : "12"}

print(len(myList))
print(myList)
myList[1] = 200
myList.insert(1, 300)
print('after')
print(myList)
print(myDict["name"])
print('after')
myDict["name"] = "KKL"
print(myDict["name"])

length = len(myList)
myList.append('ADF')

print(myList)