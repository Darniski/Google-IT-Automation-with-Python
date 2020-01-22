def area_triangles(base , height): 
    return base * height/2
    # you dont need the spaces but I like the clean look 
area_a = area_triangles(5, 4)
area_b = area_triangles(7, 3)
sum = area_a + area_b
print(sum)

# During the video your given a check point to pass 

# Use the get_seconds function to work out the amount of seconds in 2 hours and 30 minutes, then add this number to the amount of seconds in 45 minutes and 15 seconds. Then print the result.

def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2, 30, 0)
amount_b = get_seconds(0, 45, 15)
result = amount_a + amount_b
print(result)

# Passed checkpoint I deserve a sandwhich maybe
def convert_seconds(seconds): 
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60 
    return hours, minutes, remaining_seconds
hours , minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)
## More examples 