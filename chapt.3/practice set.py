# # 1. Write a python program to display a user entered name followed by Good Afternoon using input () function.
# # a=input("Enter name : ")
# # print("good morning", a.capitalize())
# # print(f"good morning {a}")  #f string for 
# # Write a program to fill in a letter template given below with name and date.
# # name=input("Enter name: ")
# # date=input("Enter date: ")
# # letter = f'''
# # Dear {name},
# # You are selected!
# # {date}
# # '''
# # print(letter)
# # another way
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
# print(letter.replace("<|Name|>", "shubham").replace("<|Date|>", "8 aug 2024")) # chaining str
# 3. Write a program to detect double space in a string.
# a="find double space  in string"
# print(a.find("  ")) #find double space
# # 4. Replace the double space from problem 3 with single spaces.
# a="find double space  in string"
# print(a.replace("  ", " ")) # replace double space with single space
# 5. Write a program to format the following letter using escape sequence characters.
letter = "Dear Harry,\nthis python course is nice.\nThanks!"
print(letter)