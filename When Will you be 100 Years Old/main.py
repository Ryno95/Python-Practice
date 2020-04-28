"""Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)"""


userName = input(
    "Dear user tell me your name and age so that I can tell you in what you will be a 100 years old: Name: "
)
userAge = input("Age: ")


if int(userAge) < 100:
    year = 2020 + (100 - int(userAge))
    print(
        "Dear "
        + userName
        + ". You will reach the ripe age of 100 in the year "
        + str(year)
        + "!"
    )
else:
    print("Sneaky sneaky Mr." + userName + ", you are already older than 100.")
