print("This Math Calculator is Made by Marsel.")
print("=======================================")


password = "Math!"

for i in range(100, 0, -1):
    attempt = input("Please Enter the Password :")
    if attempt == password:
        break
    else: 
        print("Incorrect!")

if i == 1:
    print("Wrong Password!")
else:
    print("========")
    print("Correct!")

# List of dictionary uhh nvm the dictionary doesnt work

# Menu program
while True:
    print("# Menu")
    print("1. Plus")
    print("2. Minus")
    print("3. Multi")
    print("4. Distribution")
    print("0. Exit Program")

    menu = input("Choose Menu : ")

    if menu == "0":
        break
    elif menu == "1":
        print("========================")
        print("You've Been Choosen Plus")

        print("Please Input First Number :")
        a = int(input())

        print("Please Input Second Number :")
        b = int(input())

        hasil = a + b
        print(f"{a} + {b} = {hasil}") 

        print("====================")

    elif menu == "2":
        print("=========================")
        print("You've Been Choosen Minus")

        print("Please Input First Number :")
        c = int(input())

        print("Please Input Second Number :")
        d = int(input())

        hasil = c - d
        print(f"{c} - {d} = {hasil}") 

        print("====================")

    elif menu == "3":
        print("==========================")
        print("You've Been Choosen Multi")

        print("Please Input First Number :")
        e = int(input())

        print("Please Input Second Number :")
        f = int(input())

        hasil = e * f
        print(f"{e} x {f} = {hasil}") 

        print("====================")

    elif menu == "4":
        print("================================")
        print("You've Been Choosen Distribution")

        print("Please Input First Number :")
        g = int(input())

        print("Please Input Second Number :")
        h = int(input())

        hasil = g / h
        print(f"{g} : {h} = {hasil}") 

        print("====================")

    else:
        print("You've been choosen unexist menu!")

print("Program is Done, Goodbye!")
