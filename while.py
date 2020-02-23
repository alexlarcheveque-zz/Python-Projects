L = []

while len(L) < 3:
    new_name = input("Please enter a new name: ").strip().capitalize()
    L.append(new_name)

print("Sorry the list is full.")
print(L)
