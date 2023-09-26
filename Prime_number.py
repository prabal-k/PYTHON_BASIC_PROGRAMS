# TO CHECK IF THE USER GIVEN NUMBER IS PRIME OR NOT
# 1 IS NOT A PRIME NUMBER
# The prime numbers from 1 to 100 are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
ch="y"
while(ch=='y'):
    def check_prime(num):
        count=0;
        for i in range (1,num+1):
            if(num%i==0):
                count=count+1
        if(count==2):
            print(f"{num} is prime number")
        else:
            print(f"{num} is not a prime number")


    number=int(input("Enter the number to check if it is prime or not: "))
    check_prime(number)
    ch=input("Again ? [Y/N] ").lower();
