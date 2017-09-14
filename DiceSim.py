import random as rnd

def main():
    print("***============***")
    print("Welcome to the Dice Simulator")
    print("***============***")

    max = input("Insert the number of sides of the Virtual Dice:")
    temp = menu()
    while not(temp == "Q"):
        print(temp)
        print("\n")
        if temp == "r":
            dice = rnd.randint(1, int(max))
            print("**The roll of the Virtual Dice is**: {0}".format(dice))
        else:
            print("_*_*Please select a choise from the MENU_*_*\n")
        temp = menu()

def menu():
    print("\n         **__MENU__**")
    print("--Press 'Q' to close the program")
    print("--Press 'r' to Roll the Virtual Dice")
    ans = input("\nInsert your answer here: \t")
    return ans

main()
