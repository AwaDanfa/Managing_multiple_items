""" Manage a number of items in an ordered structure
The Queue
For this task you are required to use your knowledge of lists from the Coding Preparation section to manage a number of items in an ordered structure.
You are going to be creating a program that represents the movements of the line for the lady's bathroom.
To begin, create a list that represents the line, it must contain the five names of the women initially waiting(you can make these up).
The following events occur, and you must represent them in the list and print the list out after each action.

A woman named Jenny arrives who only wanted to check her lipstick, she asks to join the front of the line, and all the women let her.
The woman third in line’s phone started ringing, and she left the line to answer.
A new woman named Alice joined the line. """

line = ["Marion", "Chantal", "Caroline", "Estelle", "Valerie"]
print(line[0])
print(line[1])
print(line[2])
print(line[3])
print(line[4])

# Jenny is on the front line - insert method
line.insert(0, "Jenny")
print(line)
# new list: ['Jenny', 'Marion', 'Chantal', 'Caroline', 'Estelle', 'Valerie']

# Woman third in line (Caroline) is leaving - remove method
line.remove("Caroline")
print(line)
# new list: ['Jenny', 'Marion', 'Chantal', 'Estelle', 'Valerie']

# Add newcomer, Alice, somewhere in the line - insert
line.insert(5, "Alice")
print(line)
