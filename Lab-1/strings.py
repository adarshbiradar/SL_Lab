#!/usr/bin/python
# In this program we use the different ways of ectracting a substring from a string
# We also deal with the string functions like split, replace and we performed concatenation using '+' operator
# At the end we use "type()" to find the type of data we are working with


print("\n Demo: String Manipulations")
mystr = "Hungry Kya!"

print(mystr)
print(mystr[0])
print(mystr[2:5])
print(mystr[2:])
print(mystr*2)
print(mystr+" Abe Nahin")
print("Length is ",len(mystr))
print("Replacing ",mystr.replace("Kya","?"))
print("Splitting ",mystr.split(" "))

print("\n Demo Number - Python can handle integer, float and complex")

x = 33
y1 = 9.87
y2 = 87.7e100
z = 4j
print(type(x))
print(type(y2))
print(type(y1))
print(type(z))
