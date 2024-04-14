import random

nameuser = "Guest"
sodu = 0

def ktmoney():
    return sodu > 0

def welcome():
    print("===============================")
    print("    WELCOME TO MINIGAME")
    print("Hi '" + nameuser + "' welcome")
    print("Your balance: " + str(sodu) + "$")

def homepage():
    print("=============================")
    print("ENTER YOUR CHOICE")
    print("1).Setup profile")
    print("2).Check your balance")
    print("3).Deposit money")
    print("4).Start game")
    print("5).Exit")
    print("6).Credit")
    print("WARNING!!! PLEASE READ THE CONTENT IN THE CREDIT")
    print("=============================")

def setupprofile():
    global nameuser
    print("\n=============================")
    print("SET UP PROFILE ZONE")
    print("Hi welcome to Setup profile page")
    nameuser = input("Let's tell us your name: ")
    print("I will remember, your name is " + nameuser)
    print("Thank you so much\n")

def checkmoney():
    print("\nThe current amount is: " + str(sodu) + "$\n")

def addmoney():
    global sodu
    print("\n=============================")
    print("     BANK")
    nap = int(input("Enter amount you want add to your account: "))
    if nap < 0:
        print("Invalid amount!")
        return
    print("Successful manipulation")
    print("Received successfully " + str(nap) + "$ into " + nameuser + " account")
    sodu += nap
    print("Total current balance: " + str(sodu) + "$\n")

def credit():
    print("\n==================================")
    print("          **CREDIT PAGE**")
    print("    ***PLEASE READ IT CAREFULLY***")
    print("1).This project is just for fun. #J4F")
    print("2).The project has NO incentive to gamble")
    print("3).Project written by Khoi")
    print("==================================\n\n")

def random1():
    return random.randint(0, 2**32 - 1)

def random2():
    return random.randint(3, 50)

def main():
    global sodu
    welcome()
    homepage()
    luachon = int(input("Enter your choice: "))

    if luachon < 1 or luachon > 6:
        print("Invalid choice! Please choose between 1 and 6.")
        return main()

    if luachon == 1:
        setupprofile()
        return main()
    elif luachon == 2:
        checkmoney()
        return main()
    elif luachon == 3:
        addmoney()
        return main()
    elif luachon == 4:
        print("\n==================================")
        print("          **PLAY ZONE**")
        if not ktmoney():
            print("Your balance is not enough, please top up.")
            addmoney()
            return main()
        else:
            betchosse = input("Type 'c' for even and 'l' for odd: ")
            if betchosse != 'c' and betchosse != 'l':
                print("Invalid choice! Please choose 'c' or 'l'.")
                return main()

            betamount = int(input("Type the amount you want to bet: "))
            if betamount <= 0 or betamount > sodu:
                print("Invalid bet amount!")
                return main()

            bet3 = random1()
            bet4 = random2()
            print("Round 1: " + str(bet3))
            print("Round 2: " + str(bet4))
            print("Result: " + str(bet3 + bet4))

            if (bet3 + bet4) % 2 == 0:
                if betchosse == 'c':
                    print("YOU WIN")
                    sodu += betamount
                else:
                    print("YOU LOSE")
                    sodu -= betamount
            else:
                if betchosse == 'l':
                    print("YOU WIN")
                    sodu += betamount
                else:
                    print("YOU LOSE")
                    sodu -= betamount

            choice = int(input("1. Continue playing\n2. Back to main menu\n3. Exit\nEnter your choice: "))

            if choice == 1 or choice == 2:
                return main()
            elif choice == 3:
                return 0
            else:
                print("Invalid choice! Exiting...")
                return 0
    elif luachon == 5:
        print("Thank you, see you later '" + nameuser + "'\n\n\n\n")
    elif luachon == 6:
        credit()

if __name__ == "__main__":
    main()
