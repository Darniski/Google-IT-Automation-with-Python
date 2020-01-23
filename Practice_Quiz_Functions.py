#This function converts miles to kilometers (km). Complete the function by having it return the result, then call the function to convert 55 miles, and print "The distance in kilometers is " with the result of the function. Then calculate the round-trip in kilometers by doubling it, and print "The round-trip in kilometers is " with that number.
def convert_distance(miles):
    km = miles * 1.6  # approximately 1.6 km in 1 mile
    return km 
distance = convert_distance(55)
print("The distance in kilometers is " + str(distance))
print("The round-trip in kilometers is " + str(distance * 2))

#  This function sorts 2 numbers and returns them in increasing order. Complete the function call, so that the resulting numbers are displayed in order.

def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)

# My solutions had a bit of a brain fart but it worked out 