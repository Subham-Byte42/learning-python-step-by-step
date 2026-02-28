# #This file contains python input output practice questions

#         #Take name as input and print: Hello, name!
name=input("Enter your name here: ")
print("Hello,",name,"!")

        #Take age as input and print how old you will be after 5 years.
age=int(input("Enter age: "))
future_age=age+5
print("Age after 5 years:",future_age)

        #Take two numbers as input and print their sum
a=int(input("Enter a: "))
b=int(input("Enter b: "))
sum=a+b
print("Sum of a and b: ",sum)

        #Take a float number as input and print its square
a=float(input("Enter the float number: "))
square=a*a
print("The square of a: ",square)

        #Take two inputs: name and favorite color, then print them in a sentence.
name=input("Enter name: ")
fav_color=input("Enter color:")
print("The favourite color of ",name," is ",fav_color,".")

        #Take length and width as input and print the area of a rectangle.
length=int(input("Enter the length of the rectangle: "))
width=int(input("Enter the width of the rectangle: "))
area=length*width
print("The area of the rectangle: ",area)

        #  Take temperature in Celsius and print it in Fahrenheit.
c=int(input("Enter celcius: "))
f=(c*9/5)+32
print("Temp in farenheight: ",f)

        #Take a number and print whether it is positive or negative.
num=int(input("Enter number: "))
if(num>0):
    print("Positive")
else:
    print("Negative")`

        #Take marks as input and print them.
mark=int(input("Enter your marks: "))
print(mark)

        #Take 3 numbers as input and print their average.
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
avg=(a+b+c)/3
print("Avg: ",avg)