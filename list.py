Fruits=['Mango', 'oranges', 'Banana', 'Grapes']
print(Fruits)
print(type(Fruits))
# indexing
print(Fruits[2])
print(Fruits[-2])

#slicing
print(Fruits[1:4])
#create a list of the days of the week
week=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print(week)

#Display Day today
print(week[1])
print(week[3:])
#updating
Fruits[1]='Tomatoes'
print(Fruits)
#updating
#append
Fruits.append('strawberries')
Fruits.append('apple')
print(Fruits)

#insert
Fruits.insert(3,'watermelon')
print(Fruits)

week[4]='Thur'
print(week)
week.append('January')
print(week)
week.insert(4,'December')
print(week)
#.remove
Fruits.remove('watermelon')
print(Fruits)

#pop
Fruits.pop(2)
print(Fruits)

#clear
Fruits.clear()
print(Fruits)
#Delete Friday from the list
week.remove('Friday')
print(week)

#Delete the first item from the list
week.pop(0)
print(week)

