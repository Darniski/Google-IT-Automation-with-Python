# Hi this the module 1 assessement 
# 1 - 5 are multiple choice and I will not be displaying those answers only to  the code problems

# 6. Write a Python script that outputs "Automating with Python is fun!" to the screen.
print("Automating with Python is fun!")

# 7.Fill in the blanks so that the code prints "Yellow is the color of sunshine".
color = 'Yellow'
thing = 'sunshine'
print(color + " is the color of " + thing)

# 8. Keeping in mind there are 86400 seconds per day, write a program that calculates how many seconds there are in a week, if a week is 7 days. Print the result on the screen.
sec = 86400
weekdays = 7
total = ( sec *  weekdays) 
print(total) 

# 9. Use Python to calculate how many different passwords can be formed with 6 lower case English letters. For a 1 letter password, there would be 26 possibilities. For a 2 letter password, each letter is independent of the other, so there would be 26 times 26 possibilities. Using this information, print the amount of possible passwords that can be formed with 6 letters.
letters = 26
password = letters ** 6
print(password)

# 10. Most hard drives are divided into sectors of 512 bytes each. Our disk has a size of 16 GB. Fill in the blank to calculate how many sectors the disk has.
disk_size = 16*1024*1024*1024
sector_size = 512
sector_amount = disk_size / sector_size

print(sector_amount)