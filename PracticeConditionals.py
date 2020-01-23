# 2.Question 2
# Complete the script by filling in the missing parts. The function receives a name, then returns a greeting based on whether or not that name is "Taylor".

def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))



# 3.Question 3
# What’s the output of this code if number equals 10?
if number > 11: 
  print(0)
elif number != 10:
  print(1)
elif number >= 20 or number < 12:
  print(2)
else:
  print(3)

# Solution is 2 



# if a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will still use 4096 bytes of storage. A file made up of 4097 bytes will use 4096*2=8192 bytes of storage. Knowing this, can you fill in the gaps in the calculate_storage function below, which calculates the storage size needed for a given filesize?
# question 5 
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = (block_size * 2) // filesize
    # Use the modulo operator to check whether there's any remainder
    partial_block = block_size % filesize
    # Depending on whether there's a remainder or not, return the right number.
    if partial_block > 0:
        return 
    else:
      return 
# Unsure what to return here
print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192