# Just like previously I am posting my code answers only multiple choice will just say that.


# Question 1
# Complete the function by filling in the missing parts. The color_translator function receives the name of a color, then prints its hexadecimal value. Currently, it only supports the three additive primary colors (red, green, blue), so it returns "unknown" for all other colors.

def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
	elif color== "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00

# 2 - 3 where mutliple choice 

# Question 4
 # Students in a class receive their grades as Pass/Fail. Scores of 60 or more (out of 100) mean that the grade is "Pass". For lower scores, the grade is "Fail". In addition, scores above 95 (not included) are graded as "Top Score". Fill in this function so that it returns the proper grade.

 def exam_grade(score):
	if  score >= 96 :
		grade = "Top Score"
	elif score >= 60 :
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail

# Question 5  mutliple choice

# Question 6
# Complete the body of the format_name function. This function receives first_name and last_name, then prints a formatted string of "Name: last_name, first_name" if both names are not blank, or "Name: " with just one of the names, if the other one is blank, and nothing if both are blank.

def format_name(first_name,last_name):
    if len(first_name) > 0 and len(last_name) > 0:
        return ("Name: "+ last_name + ", " + first_name)
    elif len(first_name) > 0 and len(last_name) == 0:
        return ("Name: "+  first_name)
    elif len(first_name) == 0 and len(last_name) > 0:
        return ("Name: " + last_name)
    else:
        return("")
        return format_name


print(format_name("Ernest", "Hemingway"))
# Should be "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should be "Name: Madonna"

print(format_name("Voltaire", ""))
# Should be "Name: Voltaire"

print(format_name("", ""))
# Should be ""

# Question 7 
#  The longest_word function is used to compare 3 words. It should return the word with the most number of characters (and the first in the list when they have the same length). Fill in the blank to make this happen.

def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word1) <= len(word3) and len(word2) >= len(word3):
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))


# Question 8
# What’s the output of this code?
def sum(x, y):
		return(x+y)
print(sum(sum(1,2), sum(3,4)))

# output is 10 

# Question 9 multiple choice 

# Question 10 
# The fractional_part function divides the numerator by the denominator, and returns just the fractional part (a number between 0 and 1). Complete the body of the function so that it returns the right number. Note: Since division by 0 produces an error, if the denominator is 0, the function should return 0 instead of attempting the division.

def fractional_part(numerator, denominator):
	if denominator != 0:
	  return (numerator % denominator) / denominator
	return 0


print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0

# Had trouble with a couple but thru python tutor I was able to power through on to week 3 !!!
