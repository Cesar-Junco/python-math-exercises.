import math

#Circumference and Area of a circle
radius = float (input("Enter a radius of a circle :"))
circumference = 2 * math.pi * radius
print(f"The circumference is : {round(circumference, 2)}cm")

# Area of a circle
r = float( input("Enter the radius of the circle: "))
area_of_circule = math.pi * pow(radius, 2 ) 
print(f"The area is :,  {round (area_of_circule, 2)}cm^2 " )

#Hypotenuse of a right triangle
a = float (input("Enter o valor de a:"))
b = float (input("Enter o valor de b:"))
hypotenuse = math.sqrt(pow(a,2) + pow(b,2))
print(f"The hypotenuse is : {round (hypotenuse, 2)}")