myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
name = input("What is your name? ")
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
mood = input("how have you been feeling lately?") 
print("{}, dont be a {} {} {}! you'll be fine" .format(name,mood,color,animal))
