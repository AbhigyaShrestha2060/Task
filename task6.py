#def cmd(keh):
#     z=keh[0]+keh[1]+keh[2]
#     print(z)
# cmd(5,7,8)

# # 4. Find the largest item from a given list.
# # x=[1,2,3,4,5,6,7,8]

# x=[1,2,3,4,5,6,7,8]
# print(max(x))

# # 5. What is the difference between 10 / 3 and 10 // 3?
# a=10
# b=3
# c=a/b
# d=a//b
# print(c)
# print(d)

# # 6. What about two asterisks (**)?
# a=5
# b=3
# c=a**b
# print(c)

 

# # 8. Write a function called fizz_buzz that takes a number.
# # If it is divisible by 5, it should return “Buzz”.
# # If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# # Otherwise, it should return the same number.
# # If the number is divisible by 3, it should return “Fizz”.

# def fizz_buzz(a):
#     if a%3==0 and a%5==0:
#         return "fizz_buzz"
#     elif a%3==0:
#         return "fizz"
#     elif a%5==0:
#         return "buzz"
#     else:
#        return "No result"    
# a=int(input("Enter a number"))
# print(fizz_buzz(a))  


# # 9.Write a function for checking the speed of drivers. 
# # If speed is less than 70, it should print “Ok”.
# # if the speed is 80, it should print: “Warning”

# def keh(speed):
#     if speed<70:
#         print("ok")
#     elif speed>80:
#         print("warning")
#     else:
#         print("Drive")
# speed=int(input("Enter a speed"))
# keh(speed)

# 10. Write a program that prompts the user to input a positive integer. It should then print the multiplication table of that number. 

# a=int(input("Enter a positive integer"))
# for i in range(1,11):
#     print(a,"x",i,"=",a*i)



# # 11. Write a program that prompts the user to input an integer and then outputs the number with the digits reversed. For example, if the input is 12345, the output should be 54321.
# n = 4562
# rev = 0  
# while(n > 0):
#     a = n % 10
#     rev = rev * 10 + a
#     n = n // 10  
# print(rev)

# # 12. Write a python program that return the number of characters in a string. 
# mylist = "Parameter"
# print(len(mylist))

# # 13. Write a Python program to multiply all the numbers in a list using while and for loop.

# def multiply(numbers):  
#     total = 1
#     for x in numbers:
#         total *= x  
#     return total  
# print(multiply((8, 2, 3, -1, 7)))

# # 14. Write a Python program to sum all the numbers in a list using for loop and while loop.

# def sum(numbers):
#     total = 0
#     for x in numbers:
#         total += x
#     return total
# print(sum((8, 2, 3, 0, 7)))

# # 18. Write a Python program to print the even numbers from a given list. 

# a=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# for keh in a:
#     if keh%2==0:
#         print(keh,end="")

# # 19. Write a Python program to print the odd numbers from a given list. 

# a=[1,2,3,4,5,6,7,8,9]
# for num in a:
#     if num%2 !=0:
#         print(num,end="")

# # 20. Write a program to accept percentage and display the Category according to the  following criteria :
# percentage=int(input("enter a percentage"))
# if percentage>=65:
#     print("Excellent")
# elif percentage>=55 and percentage<65:
#     print("Good")
# elif percentage>=41 and percentage<55:
#     print("Fair")
# elif percentage<41:
#     print("Failed")
# else:
#     print("Kati garnu programming")



# num = int(input("Enter a number: ")) 
# if num < 0:
#    print("Please enter a positive number")
# else:
#    sum = 0
# while(num > 0):
#        sum += num
#        num -= 1
#        print("The result is", sum)


