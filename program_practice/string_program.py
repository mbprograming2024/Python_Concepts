# # # Python Program to Check if a String is a Pangram or Not
# Problem Solution
# 1. Take a string from the user and store it in a variable.
# 2. Pass the string as an argument to a function.
# 3. In the function, form two sets- one of all lower case letters and one of the letters in the string.
# 4. Subtract these both sets and check if it is equal to an empty set.
# 5. Print the final result.
# 6. Exit.

# from string import ascii_lowercase as asc_lower
# def check(s):
#     return set(asc_lower) - set(s.lower()) == set([])
# strng=input("Enter string:")
# if(check(strng)==True):
#       print("The string is a pangram")
# else:
#       print("The string isn't a pangram")
# ##############################################################################
# # Python Program to Remove Odd Indexed Characters in a string

# def remove_odd_later(sub):
#     new_str=""
#     for x in range(len(sub)):
#         if x%2==0:
#             new_str+=sub[x]
#     return new_str

# str = input("Enter a string : ")

# newstr=remove_odd_later(str)
# print(newstr)

# ##############################################################################
# # Python Program to Remove the nth Index Character from a Non-Empty String

# def remove_charcter_from_index(str,index):
#     new_str = ""
#     for x in range(len(str)):
#         if x!=index:
#             new_str+=str[x]
#     return new_str

# new_str = remove_charcter_from_index("mayurbaviskar",7)
# print(new_str)


# ##############################################################################
# # Python Program to Replace All Occurrences of ‘a’ with $ in a String

# def replace_charactor(str,actualchar,replacechar):
#     return str.replace(actualchar,replacechar)


# str = "mayurbaviskar"
# actualchar = "a"
# replacechar= "$"

# print(replace_charactor(str,actualchar,replacechar))
 
# # ##############################################################################
# # Python Program to Replace Every Blank Space with Hyphen in a String

# def replace_blank_Space_with_hyphen(str):
#     return str.replace(" ","/")

# str="mayur baviskar"
# print(replace_blank_Space_with_hyphen(str))


# ##############################################################################
# Python Program to Reverse a String using Recursion

# def reverse(string):
#     if len(string) == 0:
#         return string
#     else:
#         print("str1=",string[1:])
#         print("str2=",string[0])
#         return reverse(string[1:]) + string[0]
# a = str(input("Enter the string to be reversed: "))
# print(reverse(a))




# def reverse_str(str):
#     if len(str)==0:
#         return str
#     else:
#         return (reverse_str(str[1:]))+str[0]


# print(reverse_str("mayur"))


# ##############################################################################
# # Python Program to Reverse a String Without using Recursion

# def reverse_string(str):
#     return str[::-1]

# print(reverse_string("mayur"))


# # ##############################################################################
# # Python Program to Determine How Many Times a Given Letter Occurs in a String Recursively


# def count_of_character_in_String(str,charactor):
#     count=0
#     for x in str:
#         if charactor == x:
#             count+=1
#     return count

# str = input("Enter a string to count repetation count of charactor in string :")
# charactor = input("\nEnter a charator to count its repetation in string ")

# print(count_of_character_in_String(str,charactor))





# # ##############################################################################
# # Python Program to Find the Length of a String without Library Function


# def len_str(str):
#     count=0
#     for i in str:
#         count+=1
#     return count

# str=input("Enter a tring to count it's length :")
# print(len_str(str))



# # ##############################################################################
# # Python Program to Count the Number of Words and Characters in a String

# def count_word_charactor(str):
#     word=0
#     char=0
#     for i in str:
#         if i == " ":
#             word+=1
#         elif i != " ":
#             char+=1
#     return word+1,char

# str = input("Enter a string to count word and charactor in string : ")

# print(count_word_charactor(str))

# # ##############################################################################
# # Python Program to Count Number of Lowercase Characters in a String

# from string import ascii_lowercase


# def count_lower_Case_charactor_count(str):
#     count=0
#     for i in str:
#         if i in ascii_lowercase:
#             count+=1
#     return count

# str=input("Enter a string to count number of lowercase charactor in string : ")

# print(count_lower_Case_charactor_count(str))

# # ##############################################################################
# # Python Program to Count the Number of Vowels in a String

# def count_vowels_in_string(str):
#     vowels_list = ['a','e','i','o','u']
#     count=0
#     for i in str:
#         if i in vowels_list:
#             count+=1
#     return count

# str = input("Enter a string to count number of vawels in string : ")
# print(count_vowels_in_string(str))


# # #####################################################################
# # Python Program to Count Number of Uppercase and Lowercase Letters in a String

# from string import ascii_uppercase


# def count_lower_Case_charactor_count(str):
#     count=0
#     for i in str:
#         if i in ascii_uppercase:
#             count+=1
#     return count

# str=input("Enter a string to count number of lowercase charactor in string : ")

# print(count_lower_Case_charactor_count(str))

# 
# # ####################################################################
# # Python Program to Count the Number of Digits and Letters in a String

# from string import ascii_letters
# from string import digits
# from string import punctuation

# def count_letter_char_symbol(str):
#     letter_count=0
#     digit_count=0
#     special_char=0
#     for i in str:
#         if i in ascii_letters:
#             letter_count+=1
#         elif i in digits:
#             digit_count+=1
#         elif i in punctuation:
#             special_char+=1
#     return letter_count,digit_count,special_char


# # str=input("input string to count letters digit and special charactor : ")
# str="M@yurB@Vi$kar22Kar"
# a,b,c=count_letter_char_symbol(str)
# print(f"""letter_count={a}
#     digit_count={b}
#     special_char={c}""")


# ##############################################################################
# Python Program to Print All Permutations of a String in Lexicographic Order using Recursion






# ##############################################################################
# Python Program to Print All Permutations of a String in Lexicographic Order without Recursion


# # ##############################################################################
# # Python Program to Check if the Substring is Present in the Given String

# def check_sub_string(actualstr,substr):
#     if substr in actualstr:
#         return True
#     else:
#         return False

# a=check_sub_string("MayurBavisar","sar")
# print(a)
# # ##############################################################################
# # Python Program to Find Common Characters in Two Strings

# def check_commoncaracort_in_str(*args):
#     common_char_list=[]
#     for i in args[0]:
#         if i in args[1]:
#             common_char_list.append(i)
#     return  common_char_list

# print(check_commoncaracort_in_str("mayur","baviskar"))


# # ##############################################################################
# # Python Program to Print All Letters Present in Both Strings

# def All_Letters_Present_strings(*args):
#     set1=set()
#     str=""
#     # concatstr = len(args)
#     # print(concatstr)
#     for i in range(len(args)):
#         str+=args[i]
#     print(str)
#     set1=set(str)
#     return set1    
# print(All_Letters_Present_strings("mayur","baviskar"))



# ##############################################################################
# # Python Program that Displays which Letters are in First String but not in Second

# set1=set("mayur")
# set2=set("Baviskar")

# set3 = set1-set2
# print(set3)


# ##############################################################################
# Python Program that Displays Letters that are not Common in Two Strings

set1=set("mayur")
set2=set("Baviskar")

set3=set1.difference(set2)

print(set3)



# ##############################################################################
# ##############################################################################

# ##############################################################################
# Python Program to Create a New String Made up of First and Last 2 Characters




# ##############################################################################



# ############################################################################### 
# Python Program to Find the Larger String without using Built-in Functions

# ##############################################################################



# ##############################################################################
# Python Program to Swap the First and the Last Character of a String

# ##############################################################################
# Python Program to Sort Hyphen Separated Sequence of Words in Alphabetical Order

# ##############################################################################
# Python Program to Count the Occurrences of Each Word in a String

# ##############################################################################
# Python Program to Count Number of Vowels in a String using Sets

# ##############################################################################
# Python Program to Check if a Given String is Palindrome

# ##############################################################################
# Python Program to Check whether two Strings are Anagrams

# ##############################################################################
# Python Program to Check whether a String is Palindrome or not using Recursion

# ##############################################################################
# Python Program to Find All Odd Palindrome Numbers in a Range without using Recursion