fruits=('mango', 'oranges', 'Banana', 'Grapes')
print(fruits)
print(type(fruits))

#index
print(fruits[2])
#slicing
print(fruits[1:4])

#convert to list
fruits=list(fruits)
print(fruits)
#modify
fruits[2]="strawberry"
print(fruits)
#add
fruits.append('watermelon')
print(fruits)

#convert back to tuple
fruits=tuple(fruits)
print(type(fruits))

days=("monday","Tuesday","wednesday","Thursday","Friday","saturday","sunday")
#find wednesday using an index
print(days[2])
#using a function find the length of the tupple
print(len(days))

#Replace thursday with thurs
days=list(days)
days[3]="Thur"
days=tuple(days)
print(days)