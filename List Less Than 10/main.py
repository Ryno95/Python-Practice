randomList = [
    1,
    1,
    2,
    3,
    5,
    8,
    13,
    21,
    34,
    55,
    89,
]
listBiggerthan10 = []
for element in randomList:
    if element > 10:
        listBiggerthan10.append(element)

print(listBiggerthan10)

# Putting line 14 to 19 in one line:
# print([number for number in randomList if number > 50])
# listBiggerthan10 = [number for number in randomList if number > 50]


userNumber = int(input("please enter a number between 0 and 100: "))

print(
    "Here are all numbers smaller than " + str(userNumber),
    [number for number in randomList if number < userNumber],
)
