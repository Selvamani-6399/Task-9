# Write a python code using lambda function to check every element of a list is an integer or string

check = lambda x: f"{x} is an integer" if isinstance(x, int) else f"{x} is a string" if isinstance(x, str) else f"{x} is neither an integer nor a string"
print(check(8)) 
print(check("hello")) 
print(check(3.14))
