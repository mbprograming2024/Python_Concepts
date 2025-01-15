###############################################################################
# # Python Program to Check Whether a Given Number is Even or Odd using Recursion

# def check_even_odd(num):
#     if num%2==0:
#         print(str(num)+"number is even")
#     else:
#         print("number is odd")

# num = int(input("enter a number you want to check it is even or odd \n"))

# check_even_odd(num)

###############################################################################
# # Python Program to Check Whether a Number is Positive or Negative

# def check_positive_or_negative(num):
#     if num>=0:
#         print("number is positive")
#     else:
#         print("Number is negative")


# check_positive_or_negative(-6)

###############################################################################
# # Python Program to Print All Odd Numbers in a Range

# def odd_number_in_range(start,end):
#     count=0
#     for i in range(start,end+1):
#         if i%2!=0:
#             count+=1
#             print(i)
#         else:
#             pass
#     return count

# print(odd_number_in_range(1,30))

###############################################################################
# # Python Program to Check if a Number is a Palindrome

# def check_palindrome(num):
#     revernum = num[::-1]
#     if num == revernum:
#         print("number is palindrom")
#         print("actual number",num)
#         print("After reverse number",revernum)
#         print("both reverse and actual number is same hence we can say number is palindrom")
#     else:
#         print("number is not palindrom")
#         print("actual number",num)
#         print("After reverse number",revernum)

# num = (input("enter a number to check it is palindrome or not"))
# print(num)
# check_palindrome(num)

###############################################################################
# # Python Program to Reverse a Number

# def reverse_number(num):
#     reverse_num = str(num)[::-1]
#     return reverse_num


# num=1587463

# print(reverse_number(num))

###############################################################################
# # Python Program to Print All Integers that Aren’t Divisible by Either 2 or 3

# count=0
# for i in range(1,100):
#     if(i%2!=0 and i%3!=0):
#         count+=1
#         print(i)
#     else:
#         pass

# print("total Count",count)



###############################################################################
# # Python Program to Find Numbers which are Divisible by 7 and Multiple of 5 in a Given Range

# count=0
# for i in range(1,100):
#     if i%7==0 and i%5==0:
#         count+=1

###############################################################################
# # Python Program to Print All Numbers in a Range Divisible by a Given Number

# def number_divisibility(start,end,divisor):
#     for i in range(start,end):
#         if i%divisor==0:
#             print(i,"is divisible by ",divisor)
        
# number_divisibility(1,50,6)

###############################################################################
# # Python Program to Find Sum of Digits of a Number


# def addition_of_digits_in_num(num):
#     add=0
#     for i in num:
#         add+=int(i)
#     return add

# num=input("Enter a number")

# sum_of_digits = addition_of_digits_in_num(num)
# print(sum_of_digits)


###############################################################################
# Python Program to Find Sum of Digit of a Number using Recursion







###############################################################################
# Python Program to Find Sum of Digit of a Number Without Recursion

# # Python Program to Count the Number of Digits in a Number

# num = input("enter a number")

# for i in num:
#     if i.isdigit():
#         print("\'"+i+"\'"+"it is digit")
#     else:
#         print(i,"it is not digit")



###############################################################################
# Python Program to Find All the Divisors of an Integer

###############################################################################
# Python Program to Find the Smallest Divisor of an Integer

###############################################################################
# Python Program to Print Binary Equivalent of an Integer using Recursion

###############################################################################
# Python Program to Print Binary Equivalent of a Number without Using Recursion



###############################################################################
# Python Program to Print Table of a Given Number


# def table_of_num(num: int):
#     for i in range(1,10):
#         print(num*i)

# def table_of_num2(num):
#     for i in range(1,10):
#         print(int(num)*i)



# num=input("Enter a number to print its table=")
# table_of_num(num)


# Python Program to Calculate Grade of a Student



# Python Program to Check if a Date is Valid and Print the Incremented Date if it is

# # Python Program to Check Whether a given Year is a Leap Year

# def check_leap_year(year):
#     if (year%4==0 and year%100!=0 or year%400==0):
#         print(year,"is leap year")
#     else:
#         print(year,"not an leap year")

# year = int(input("enetr year to  check it is leap year or not"))
# check_leap_year(year)



# Python Program to Convert Centimeters to Feet and Inches

# def convert_centimeter_feet_inches(centimeter,unit):
#     match unit:
#         case feet:
#             feets = round((1/30.38)*centimeter,4)
#             return feets
#         case meters:
#             meters = centimeter*0.01
#             return meters
# print(convert_centimeter_feet_inches(1,"feet"))

# Python Program to Read a Number n and Compute n+nn+nnn
