#Ask user for name

name = input("What is your name?: ")

#Ask users for age

age = input("What is your age?: ")

#Ask users for city

city = input("What is your city?: ")

#What they enjoy

hobbies = input("What do you enjoy?: ")

#Create output text

string = "Your name is {} and you are {} years old. You live in {} and you enjoy {}"
output = string.format(name, age, city, hobbies)

#Print output to screen

print(output)
