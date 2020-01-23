#example of username check for characters less then 3 video example
def hint_username(username):
    if len(username) < 3: 
        print("Invalid username. Must be at least 3 characters long")
    else: 
        print("Valid username")

# solution to video check 
def is_positive(number):
  if number > 0:
    return True 
  else:
    return None

# else statment video 
def is_positive(number):
  if number > 0:
    return True 
  else:
    return False 

#modulo 
def is_even(number)
     if number % 2 == 0:
         return True
    return False # even though the else statment isnt here and this will run and end depend on the output 

    def hint_username(username):
    if len(username) < 3: 
        print("Invalid username. Must be at least 3 characters long")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long")
    else: 
        print("Valid username")

#Solution to the elif video check 
def number_group(number):
  if number > 0:
    return "Positive"
  elif number < 0:
    return "Negative"
  else:
    return "Zero" 

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative 