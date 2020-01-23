# So this excercise covers writing better clear code

#Example 
def calculate(d): 
    q = 3.14
    z = q * (d ** 2) 
    print(z)
calculate(5)

# Better expressed example 
def circle_area(radius): 
    pi = 3.14
    area = pi * (radius ** 2) 
    print(area)
circle_area(5)


#This function to calculate the area of a rectangle is not very readable. Can you refactor it, and then call the function to calculate the area with base of 5 and height of 6? Tip: a function that calculates the area of a rectangle should probably be called rectangle_area, and if it's receiving base and height, that's what the parameters should be called.

# exercise

def f1(x, y):
	z = x*y  # the area is base*height
	print("The area is " + str(z))
f1(5, 6)

# My solution

def rectangle_area(base,height):
	sum = base * height  # the area is base*height
	print("The area is " + str(sum))
rectangle_area(5, 6) 

# (Hashtag) Solved.