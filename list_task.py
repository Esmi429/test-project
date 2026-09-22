#create a new file list_task.py
#trainees = ["John", [2, ["James","Mary"]]]
#Display 2 from the list.
#Output James  from the list.
#Using a method add 56 at the end of the list.
#Using a method add the name Mike between James and Mary
#Change the value of 2 to 8
#Remove John and Mary from the list.
#Using a function, determine the length of the list
trainees=["John", [2, ["James", "Mary"]]]
print(trainees[1][0])
trainees=["John", [2, ["James", "Mary"]]]
print(trainees[1][1][0])

trainees=["John", [2, ["James", "Mary"]]]
trainees.append(56)
print(trainees)

trainees=["John", [2, ["James", "Mary"]]]
trainees[1][1].insert(1, "Mike")
print(trainees)
trainees=["John", [2, ["James", "Mary"]]]
trainees[1][0]= 8
print(trainees)

trainees=["John", [2, ["James", "Mary"]]]
trainees.remove("John")
trainees[0][1].remove("Mary")
print(trainees)

trainees=["John", [2, ["James", "Mary"]]]
print(len(trainees))

