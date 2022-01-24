name = input("Enter your first name: ")
value = 0
for c in name:
    value += ord(c)

print(name, "becomes", value)
