"""""
x = input("What's x?  ")
y = input("What's y?  ")

z = x + y This would treat the input as a string, simply printing the numbers side-by-side instead of adding them.
At this point, we need to  create integers:

z = int(x) + int(y)
print(z)
Simplified below:
"""
x = int(input("What's x?  "))
y = int(input("What's y?  "))

print("y + x =  ", x + y)
