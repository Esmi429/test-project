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

# 2. Display "Brian" from the list.

# 3. Display "Alice" from the list.

# 4. Using a list method, add the number 7 at the end of the outer list.

# 5. Add "David" between "Brian" and "Alice".

# 6. Change the number 4 to 10.

# 7. Change "Kevin" to "James".

# 8. Remove "TechElar" from the list.

# 9. Remove "Alice" from the nested list.

# 10. Add "Mary" at the beginning of the nested list.

# 11. Using len(), find the number of items
#     in the nested employee list.

# 12. Print the final list.

