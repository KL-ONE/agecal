#TITLE = SIMPLE CURRENT AGE CALCULATOR 
#AUTHOR = SIDDHANT DOLAS
#LANGUAGE = PYTHON 3


# THIS IS FOR HEADING
print("x" * 55)
print(" W E L C O M E   U S E R")
print("x" * 55)
print()
print()


# GET USER NAME
print("x" * 55)
name = str(input("ENTER YOUR NAME: "))
print("x" * 55)

# PRINT MESSAGE
what = str("Let's Calculate Your Current Age!")
print()
print()
print("x" * 55)
print(what)
print("x" * 55)
print()
print()
print("x" * 55)

# GET USER INFORMATION DATA
current = int(input("ENTER CURRENT YEAR: "))
birth_year = int(input("ENTER BIRTH YEAR: "))
print("x" * 55)

# FORMULA TO CALCULATE CURRENT AGE OF USER
sum = int(current) - int(birth_year)
msg = "YOU ARE"
msg_2 = "YEARS OLD"
print()
print()

# PRINT OUTPUT
print("x" * 55)
print(msg, sum, msg_2)
print("x" * 55)

# CODE END HERE


