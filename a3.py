import random
rand = random.randint(1, 20)
#print(rand)

x = input("Enter your First Name:")
y = input("Enter your Last Name:")
z = eval(input("Enter your OTP Number(1-20):"))

if z == rand:                                       # if number matches the random number
    print("OTP SUCCESSFULLY MATCHED")
else:
    print("ERROR!!! ENTER THE OTP AGAIN")

for i in range(0,3):
        again = input("DO YOU WANT TO ENTER AGAIN??(Enter 'yes' or 'no')")

        if again.lower() == "yes":
            z = eval(input("Enter your OTP Number(1-20):"))
        elif again.lower() == "no":
            print("THANKS FOR ATTEMPT")
            break
        if z == rand:
            print("OTP SUCCESSFULLY MATCHED")
            break
        if i == 2:
            print("SORRY PROGRAM CRASHED")