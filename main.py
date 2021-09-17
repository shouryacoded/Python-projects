import math
import random
# 1

print("Hello World") 

#2

first = input("Enter the first number : ")
second = input("Enter the second number : ")
print("The sum of the number are : ", int(first)+int(second))


#3

num = input("Enter a number to sqaure root : ")
print(math.sqrt(float(num)))

#4

print("Enter the three sides of the triangle to find the area.")
a = float(input("Enter side A : "))
b = float(input("Enter side B : "))
c = float(input("Enter side C : "))
s = (a+b+c)/2
area =  math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of the trinagle : ", area)


#5 

print("Enter the coefficients of the quadratic to find the roots.")
a1 = float(input("a : "))
b1 = float(input("b : "))
c1 = float(input("b : "))
d = math.sqrt(b1*b1 - 4*a1*c1)
r1  = (-b1+d)/(2*a1)
r2  = (-b1-d)/(2*a1)
if d >= 0:
        print("root 1 : ",r1," root 2 : ",r2)
else:    
        print("The roots are imaginary")

#6

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second  number : "))
print ("Number before swapping : " , num1 , " ",num2 )
num1 = num1+num2
num2 = num1 - num2
num1 = num1 - num2
print ("Number after swapping : " , num1 , " ",num2 )
#7

print(int(random.random()))



#8

km_dist = float(input("Enter the distance in kilometers : "))
mile_dist = 0.621371 * km_dist
print("The distance in miles is : ",mile_dist)



#9
c_temp = float(input("Enter the temperature in celsius: "))
f_temp = (c_temp*1.8)+32
print("The temperature in farenheit is : ",f_temp)

#10
user_num = int(input("Enter a number : "))
if user_num > 0:
        print("The number is positive")
elif user_num < 0:
        print("The number is negative")
else:    print("The number is zero")

#11
user_num = int(input("Enter a number : "))
if user_num % 2 == 0:
        print("The number is positive.")
else:   print("The number is odd.")

#12

user_year = int(input("Enter a year : "))
if user_year%4 == 0:
        if user_year %100 == 0 : 
                if user_year % 400 == 0:
                        print("The year is leap year")
                else:   print("Not a leap year")
        else:
                print("This year is leap year")
else:
        print("Not a leap year")

#13

print("Enter three numbers one by one to find the maximum")
num_1 = int (input("Enter the number 1:"))
num_2 = int (input("Enter the number 2:"))
num_3 = int (input("Enter the number 2:"))
print("The maximum number : ",max(num_1,max(num_2,num_3)))


#14

prime_num = int(input("Enter a number :"))
if prime_num > 1:
        for i in range(2,prime_num) :
                if prime_num%i == 0:
                        print(prime_num," is not a prime number")
                        break
else :
        print(prime_num," is a prime number.")

#15

upper = int(input("Enter the upper : "))
lower = int(input("Enter the lower : "))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)