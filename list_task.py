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
#using a method add the name mike between James and Mary
trainees=["John", [2, ["James", "Mary"]]]
trainees[1][1].insert(1, "Mike")
print(trainees)
#change the value of 2 to 8
trainees=["John", [2, ["James", "Mary"]]]
trainees[1][0]= 8
print(trainees)
#Remove Jhon and Marry from the List
trainees=["John", [2, ["James", "Mary"]]]
trainees.remove("John")
trainees[0][1].remove("Mary")
print(trainees)
#Determine the length of the list
trainees=["John", [2, ["James", "Mary"]]]
print(len(trainees))
employees = ["TechElar",[4, ["Kevin", "Brian", "Alice"]]]

# 1. Display the number 4.
print(employees[1][0])

# 2. Display "Brian" from the list.
print(employees[1][1][1])

# 3. Display "Alice" from the list.
print(employees[1][1][2])

# 4. Using a list method, add the number 7 at the end of the outer list.
employees=list(employees)
employees.append(7)
print(employees)
employees=tuple(employees)
print(employees)

# 5. Add "David" between "Brian" and "Alice".
employees=list(employees)
employees[1][1].insert(2,"David")
print(employees)

# 6. Change the number 4 to 10.
employees[1][0]=10
print(employees)

# 7. Change "Kevin" to "James".
employees[1][1][0]= ("James")
print(employees)


# 8. Remove "TechElar" from the list.
employees.remove("TechElar")
print(employees)

# 9. Remove "Alice" from the nested list.
employees[0][1].pop()
print(employees)

# 10. Add "Mary" at the beginning of the nested list.
employees=list(employees)
employees[1][1].insert(0,"Mary")
print(employees)

# 11. Using len(), find the number of items
#     in the nested employee list.
print(len(employees))

# 12. Print the final list.

