users = []

users.append("Kevin")
users.append("Bob")
users.append("Alice")
del users[1]
users.reverse()
users.insert(1 , "Melody")
users += ["Pierre" , "Mike"]
new_users = users[0:1]

print(users)
print(new_users)


