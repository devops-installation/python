#1. Write a program to find the greatest of four numbers entered by the user.
# n1=int(input(("Enter no.: ")))
# n2=int(input(("Enter no.: ")))
# n3=int(input(("Enter no.: ")))
# n4=int(input(("Enter no.: ")))

# if(n1>n2 and n1>n3 and n1>n4):
#     print(n1, "is greater than", n2,n3,n4)
# elif(n2>n3 and n2>n1 and n2>n4):
#     print(n2, 'is greater than', n3,n1,n4)
# elif(n3>n1 and n3>n2 and n3>n4):
#     print(n3, 'is greater than', n2,n1,n4)
# elif(n4>n1 and n4>n2 and n4>n3):
#     print(n4, "is greater than", n1,n2,n3)
# else: # no need to else in elif
#     print("value is not exist")
######################################
"""
2. Write a program to find out whether a student 
 has passed or failed if it requires a total of 40% and 
 at least 33% in each subject to pass. 
 Assume 3 subjects and take marks as an input( from the user.
 """
# s1=int(input("Enter marks marathi: "))
# s2=int(input("Enter marks science: "))
# s3=int(input("Enter marks english: "))
# total_percentage=float((((s1+s2+s3)/300)*100))
# if((s1>=33 and s2>=33 and s3>=33) and (total_percentage >= 40)):
#     print("you are passed", total_percentage)
# else:
#     print("you are failed", total_percentage)

"""
A spam comment is defined as a text containing following keywords:
"Make a lot of money", "buy now", "subscribe this", "click this".
 Write a program to detect these spams.
"""
# p1 ="Make a lot of money"
# p2 ="buy now"
# p3 ="subscribe this"
# p4 ="click this"
# message=input("Enter comment: ")
# if ((p1 in message) or (p2 in message) or (p3 in message) or(p4 in message)):
#     print("This comment is a spam")
# else:
#     print('this comment not spam')
"""
4. Write a program to find whether 
a given username contains less 
than 10 characters or not.

"""
# n=input("Enter username: ")
# print(n.__len__())
# if (n.__len__()<10):
#     print(n,"Username is less than 10 character ")
# else:
#     print(n,"Username is greater than 10 character", n.__len__())
"""

"""
















