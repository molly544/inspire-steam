#Maureen Mbugua
#18/02/2026
#programme to show lists in python

friends=["Reachel","Phoebe","Ross","Monica","Joey","Chandler"]

print(friends)
friends.sort()
print(friends)
friends.reverse()
print(friends)
friends.append("Ellie")
print(friends)

new_friends=["Wendy","Cynthia","Nicky","Ricky","Dawn"]

print(len(new_friends))

#new list of students
students=friends+new_friends

print(students)

students.pop()
print(students)
students.remove("Ross")
print(students)
students.insert(5,"Jenny"),(10,"Valary")
print(students)
students.insert(10,"Valary")
print(students)
students.extend("D")
print(students)

new_students=students.copy()
print(new_students)

