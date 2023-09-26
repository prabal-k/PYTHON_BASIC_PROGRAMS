# question -1:
# write a function that takes in a list of integers and return true if it contains 007
# in order..for eg
# spy_game([1,2,4,0,0,7,5])    === TRUE
# spy_game([1,0,2,4,0,5,7)]    === True
# spy_game([1,7,2,0,4,5,0)]    === fALSE

# solution
# def check(num):
#     count=0;
#     list2=[0,0,7,'x']
#     for item in num:
#         if(item==list2[0]):
#             list2.pop(0)
#             count=count+1
#
#     if(count==3):
#         return True
#     else: return False
#
# list=[1,0,2,4,0,5,7]
# condition=check(list)
# print(condition)
# --------------------------------------------

# QUESTION-2

# write a function that returns the number of prime numbers that exist upto
# and including a given number
#    solution

# def prime_list(num):
#     count=0
#     list=[]
#     for i in range(1,num+1):
#         for j in range(1,i+1):
#             if(i%j==0):
#                 count=count+1
#
#         if(count==2):
#                 list.append(i)
#         else:
#                 count=0
#     return list
#
# num=prime_list(100)
# print(num,"\n")
# print(len(num))
# -----------------------------------------------------

# Question -3
# write a function that return the lesser of two given numbers if both numbers
# are even,but returns the greater if one or both numbers are odd

# solution
# def lesser(a,b):
#     pass
#     if(a%2==0 and b%2==0):
#         return (min(a,b))
#
#     elif(a%2!=0 or b%2!=0):
#        return (max(a,b))
#
# output =lesser(10,20)
# print(output)

# -----------------------------------------------------
# question -4
# write a function that takes a string and returns true if all the words begin with same letter

#
# def input(str):
#     list2=[]
#     list3 = []
#     list=str.lower().split(" ")
#     print(list)
#     for i in list:
#         list2.append(i[0])
#     print(list2)
#     for i in list2:
#         if i not in list3:
#             list3.append(i)
#     if(len(list3)==1):
#         return True
#     else:
#         return False
#
#
# result =input("Hello Hir how hre hou")
# print(result)

# ----------------------------------------------------------

# Question- 6
# given 2 integers ,return true if the sum of the integer is 20 or if one of the integer is 20 ..if not return false
# def sum(a,b):
#     if((a+b)==20 or (a==20 or b==20)):
#         return True
#     else:
#         return False
#
#
# res=sum(20,30)
# print(res)

# --------------------------------------------------------------

#Question -7
# write a function that capitalizes the first and fourth letter of a name

# def capt(str):
#     first_letter=str[0]
#     inbetween=str[1:3]
#     fourth=str[3]
#     remaining=str[4:]
#     print(first_letter.upper()+inbetween+fourth.upper()+remaining)
#
# capt("macdonalds")
# --------------------------------------------------------------

# Question -8
# given a sentence ,return a sentence with the words recersed

# for eg:
# (I am home) ------> (home am I)
# (We are ready) ---> (ready are we)

# def sentence(str):
#     list = str.split(" ")
#     list2=[]
#     length = len(list)
#     print(*list)
#     for i in range (length-1,-1,-1):
#         list2.append(list[i])
#
#     print(*list2)
#
# sentence("we are ready")

# --------------------------------------------------------------
# Question - 9
# Given an integer n,return True if n is within 10 of either 100 or 200

# def numbers(num):
#     if(num>=90 and num<=110):
#         return True
#     elif(num>=190 and num<=210):
#         return True
#     else:
#         return False
#
# condition = numbers(111)
# print(condition)

# --------------------------------------------------------------
# Question - 10
# Given an list of integer ,return True if the array contains a 3 next to a 3 somewhere

# (1,3,3)--->True
# (1,3,1,3)--> false
# (3,1,3)-->false

# solution-1
# def text(arr):
#     count=0
#     a=[3,3,'x']
#     for i in arr:
#         if i == a[0]:
#             a.pop()
#             count=count+1
#         else:
#             count=0
#         if(count==2):
#             break;
#     if(count==2):
#         return True
#     else:
#         return False
#
# cond=text([1,3,2,3,2,3])
# print(cond)

# --------------------------solution 2

# def text(arr):
#     ch=0
#     for i in range (0,len(arr)-1):
#             if(arr[i]==arr[i+1]==3):
#                 ch=1;
#                 break;
#     if(ch==1):
#         return True
#     else:
#         return False
#
#
# cond=text([1,3,1,4,2,3])
# print(cond)

# -------------------------------------------------------------------------
#
# Question -11
# given a string ,return a string where for every character in the original there are three characters
# ("hello")--->("hhheeellllllooo")
# ("Mississippi")--->("MMMiiissssssiiissssssiiippppppiii")

# def string(str):
#     str2=""
#     j=0;
#     for i in str:
#         for j in range(0,3):
#             str2=str2+i
#     print(str2)
# string("adw")

# -------------------------------------------------------------------------





