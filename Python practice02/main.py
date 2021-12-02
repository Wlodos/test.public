s = 0
amount = int(input("Enter amount of tickets "))
age = [int(input("Enter age ")) for i in range(amount)]

for i, value in enumerate(age):
    if 18 <= value < 25:
        s += 990
    elif value >= 25:
        s += 1390
print("Full price is", s, "Rub", end="")
if amount > 3:
    print(", but you have 10% discount and final price is", round(s*0.9), "Rub")
