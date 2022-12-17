import random


def add(a, b):
    c = a + b
    return c


def subtract(a, b):
    c = a - b
    return c


def multipy(a, b):
    c = a * b
    return c


def divide(a, b):
    c = a/b
    return c


def guessingGame():

    points = 0

    print("Great, pick a number")

    while True:
        number = input()
        if number.isdigit():
            number = int(number)
            break
        else:
            print("Choose a number with no spaces next time")
            continue

    effect = random.randint(1, 4)

    if effect == 1:
        numberAdd = random.randint(1, 100)
        newNumber = add(number, numberAdd)

        print(f"The new number is {newNumber}.\n"
              f"Can you guess how we got here?")

        guess = input()

        if guess.lower().__contains__("add"):
            print("You got it right!")

            points += 1

            print("now guess what number we added")

            while True:
                guessAdd = input()
                if guessAdd.isdigit():
                    guessAdd = int(guessAdd)
                    break
                else:
                    print("Choose a number with no spaces next time")
                    continue

            if guessAdd == numberAdd:
                print("Correct again!")

                points += 1

                return points

            else:
                print(f"sorry, that is wrong, the answer was {numberAdd}")

                return points

        else:
            print("sorry, you got it wrong, it was addition.")
            print("now guess what number we added")

            while True:
                guessAdd = input()
                if guessAdd.isdigit():
                    guessAdd = int(guessAdd)
                    break
                else:
                    print("Choose a number with no spaces next time")
                    continue

            if guessAdd == numberAdd:
                print("Correct!")

                points += 1

                return points

            else:
                print(f"sorry, that is wrong, the answer was {numberAdd}")

                return points

    if effect == 2:
        numberSub = random.randint(1, 100)
        newNumber = subtract(number, numberSub)

        print(f"The new number is {newNumber}.\n"
              f"Can you guess how we got here?")

        guess = input()

        if guess.lower().__contains__("subtract"):
            print("You got it right!")

            points += 1

            print("now guess what number we subtracted")

            while True:
                guessSub = input()
                if guessSub.isdigit():
                    guessSub = int(guessSub)
                    break
                else:
                    print("Choose a number with no spaces next time")
                    continue

            if guessSub == numberSub:
                print("Correct again!")

                points += 1

                return points

            else:
                print(f"sorry, that is wrong, the answer was {numberSub}")

                return points

        else:
            print("sorry, you got it wrong, it was subtraction.")
            print("now guess what number we subtracted")

            while True:
                guessSub = input()
                if guessSub.isdigit():
                    guessSub = int(guessSub)
                    break
                else:
                    print("Choose a number with no spaces next time")
                    continue

            if guessSub == numberSub:
                print("Correct!")

                points += 1

                return points

            else:
                print(f"sorry, that is wrong, the answer was {numberSub}")

                return points

    if effect == 3:
        numberMulti = random.randint(1, 100)
        newNumber = multipy(number, numberMulti)

        print(f"The new number is {newNumber}.\n"
              f"Can you guess how we got here?")

        guess = input()

        if guess.lower().__contains__("multi"):
            print("You got it right!")

            points += 1

            print("now guess what number we multiplied")

            while True:
                guessMulti = input()
                if guessMulti.isdigit():
                    guessMulti = int(guessMulti)
                    break
                else:
                    print("Choose a number with no spaces next time")
                    continue

            if guessMulti == numberMulti:
                print("Correct again!")

                points += 1

                return points

            else:
                print(f"sorry, that is wrong, the answer was {numberMulti}")

                return points

        else:
            print("sorry, you got it wrong, it was multiplication.")

            print("now guess what number we multiplied")

            while True:
                guessMulti = input()
                if guessMulti.isdigit():
                    guessMulti = int(guessMulti)
                    break
                else:
                    print("Choose a number with no spaces next time")
                    continue

            if guessMulti == numberMulti:
                print("Correct!")

                points += 1

                return points

            else:
                print(f"sorry, that is wrong, the answer was {numberMulti}")

                return points

    if effect == 4:
        numberDivi = random.randint(1, 100)
        newNumber = divide(number, numberDivi)

        print(f"The new number is {newNumber}.\n"
              f"Can you guess how we got here?")

        guess = input()

        if guess.lower().__contains__("divi"):
            print("You got it right!")

            points += 1

            print("now guess what number we divided by")

            while True:
                guessDivi = input()
                if guessDivi.isdigit():
                    guessDivi = int(guessDivi)
                    break
                else:
                    print("Choose a number with no spaces next time")
                    continue

            if guessDivi == numberDivi:
                print("Correct again!")

                points += 1

                return points

            else:
                print(f"sorry, that is wrong, the answer was {numberDivi}")

                return points

        else:
            print("sorry, you got it wrong, it was division.")

            print("now guess what number we divided by")

            while True:
                guessDivi = input()
                if guessDivi.isdigit():
                    guessDivi = int(guessDivi)
                    break
                else:
                    print("Choose a number with no spaces next time")
                    continue

            if guessDivi == numberDivi:
                print("Correct!")

                points += 1

                return points

            else:
                print(f"sorry, that is wrong, the answer was {numberDivi}")

                return points


print("Greetings. What is your name? ")

name = input()

if name == "Cris" or name == "Chris" or name == "Christopher":
    print("(what a great name!)")
elif name == "Cristopher":
    print("(Are you...?! never mind, let's continue.)")
else:
    print("\nnice name\n")
print(f"All right, {name}, we are gonna play a game.\n"
      f"You will type in a number, and I will return a new number.\n"
      f"You will have to guess how we got from your number to my new number.\n"
      f"It could be through multiplication, addition, subtraction or division.\n"
      f"Ready?")

choice = input()

if choice.__contains__("n" or "N"):
    print("...I see, farewell")
    quit()

points = (guessingGame())
count = 2

while True:
    print("Would you like to go again?")

    choice2 = input()

    if choice2.lower().__contains__("n"):
            print(f"You got {(points/count) * 100} percent of the questions correct!!")
            quit()
    else:
            points += guessingGame()

            count += 2

