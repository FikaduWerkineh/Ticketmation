from project1 import countdown
from project2 import activities
from project3 import message
def mainTomain():
    cosmetics = 0
    perfumes = 0
    medicine = 0
    list = [346369309, 123456789]
    cou = 0
    ID = int(input("please insert your id: "))
    while cou < 3:

        if ID in list:
            order = activities()
            if order == "c":
                cosmetics += 1
                print("_________________")
                print("Your number is:", f"C -{cosmetics}")
                message()
            elif order == "p":
                perfumes += 1
                print("_________________")
                print("Your number is:", f"P -{cosmetics}")
                message()
            elif order == "m":
                medicine += 1
                print("_________________")
                print("Your number is:", f"M -{cosmetics}")
                message()
            stoping = input("Do you want to take another number y/n ?")
            if stoping == "n":
                break
        else:
            cou = 0
            while cou < 3:
                y = int(input("Invalid id, please enter again:"))
                cou = cou + 1
            countdown(30)