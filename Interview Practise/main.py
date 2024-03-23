# Reverse a String

# The[::-1] notation means "start from the end, go all the way to the beginning, and take steps of -1" which effectively reverses the string.
# So, s[::-1] takes the entire string s and reverses it.
# def rev(s):
#     print(s[::-1])
#
# rev("hello")

# Check if a String is Palindrome:

# def pallindrome(s):
#     s=s.lower();
#     r=s[::-1]
#     if s==r:
#         print("True")
#     else:
#         print("False")
#
# pallindrome("AmanaplanacanalPanama")

# Find the Factorial of a Number:

# def fact(s):
#     if(s==0):
#         return 1
#     else:
#         return (s*fact(s-1))
#
# result=fact(6)
# print(result)

#Check for a prime number:

# def check(num):
#     count=0;
#     if num<=1:
#         return False
#     else:
#         for i  in range(2,num):
#             if (num%i==0):
#                 return False
#
#         return  True
#
# res=check(11)
# print(res)

# def fibonacci(num):
#     a=0;
#     b=1;
#     print(a," ",b);
#     for i in range(2,num):
#         c=a+b;
#         a=b;
#         b=c;
#         print(c," ");
#
# fibonacci(10)


# def two_sum(nums,target):
#     nums_index={};
#     for i,num in enumerate(nums):
#         complement=target-num;
#         if complement in nums_index:
#             return [nums_index[complement],i]
#
#         nums_index[num]=i;
#
#
#
# nums=[2,7,11,15];
# target=17
# print(two_sum(nums,target))

#
# my_string = "Hello World"
# print(my_string[3:10])

# ----------------------------------lambda function in python-------------------

# k=lambda x,y: y if y%2==0 else x;
# print(k(2,3))
def lm(fx,value):
        return 2*fx(value)

print(lm(lambda x:x*2,3))


# ----------------------------------LIST in python-------------------

# 1)
# names=['prabal','rahul','simon','satish','bikash','ramesh',''];
# print("length:",len(names))
# names.append('john')
# for n in names:
#         print(n,end=',')
# print("length:",len(names))

# 2)
# id=[1,34,12,56,2]
# x=input("Enter a number: ")
# id.append(x)
# if x in id:
#         print('yes')
# else:
#         print('no')
#




# ----------------------------------dictonary in python-------------------
# 1)
# dict1={'first_name':'john','lastname':'kc'}
# print(dict1['first_name'])

# 2)
# dict = [{'name':'prabal','sirname':'kuinkel','middlename':'tapri','job':'director'},
#         {'name':'ramesh','sirname':'neupane','middlename':'chapri','job':'actor'},
#         {'name':'bikash','sirname':'khanal','middlename':'a','job':'producer'}];
# for n in dict:
#         if(n['job']=='director'):
#                 print(n['name'])
#
#
#

    















