import json 

filename = 'userName.json'
name = ''
#Check for a history fiel 
try:
    with open(filename, "r") as r:
        #Load the user's name from the history file
        name = json.load(r)
except IOError:
        print ("First-time login")
#If the user was found in the histiry file, welcome them back 
if name != "":
    print("welcome back"+ name + "!")
else: 
    # if the history file doesnt exist, ask the user for their name
    name = input("hello! what's your name?")
    print ("Welcome," + name + "!")
# Save the user's name to the history file
try:
    with open(filename, 'w') as f:
        json.dump(name, f)
except IOError:
    print("There was a problem writing to the history file.")

