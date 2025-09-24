num = int(input("Enter your number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("The number you entered is not a prime number")
            break
    else:
        print("The number you entered is a prime number")
else:
    print("The number you entered is not a prime number")