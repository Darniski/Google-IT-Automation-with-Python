# functions in python 3 

def greeting(name, department ):
    print("Welcome, "    + name)
    print ("Your are part of " + department)

greeting("Darnell", "Software egineering")
print(greeting)
 # Example function 


# Challenge Function

# Do you think you can flesh out your own function? I think you can! Let’s give it a go.

# Flesh out the body of the print_seconds function so that it prints the total amount of seconds given the hours, minutes, and seconds function parameters. Remember that there are 3600 seconds in an hour and 60 seconds in a minute.


def print_seconds(hours, minutes, seconds):
    print(3600 * hours + 60 * minutes + 1 * seconds)

print_seconds(1,2,3)

# Woohoo got it correct 