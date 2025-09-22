correct_password = "1234"
user_password=input("enter your password: ")

while user_password != correct_password:
    print("wrong password ,try again")
    user_password = input("enter your password: ")

print("Access granted!")
