import random

print("""Greetings - let's play a game. You'll get five attempts to guess
my secret number, so choose wisely. Good luck!\n""")

#function utilized in event of redunant user input
def dejavu(guess, guesses):

    if guess in guesses:
        print("\nOops, you've already guessed that number!\n")
        return True
    else:
        return False

#main game-guessing program
def guessing_game():

    secret_num = random.randint(1, 100)
    guesses = []

    while len(guesses) < 5:

        try:
            guess = int(input("Please guess a number between 1 and 100: "))
            has_already_guessed = dejavu(guess, guesses)

            if has_already_guessed:
                guesses.append(guess)
                continue

        except ValueError:
            print("Nice try, but {} isn't a number! Please guess again: ".format(guess))
            break

        except UnboundLocalError:
            print("Nice try, but I'd recommend typing an actualy number! Please try again: ".format(guess))
            break

        else:
            if guess == secret_num:
                print("\nWell played, my friend; my number was {}, and it only took you {} guesses!".format(secret_num, len(guesses)))

                break

            elif guess < secret_num:
                print("\nClose, but my number is definitely higher than {}.\n".format(guess))
                guesses.append(guess)

            else:
                print("\nNope! My number is definitely lower than {}.\n".format(guess))
                guesses.append(guess)

    else:
        print("\nAhhh, bummer! You guessed {} times but didn't quite make it! The secret number was {}.".format(len(guesses), secret_num))

        play_again = input("Do you want to play again? Y/n ")

    if play_again.lower() != 'n':
        guessing_game()
    else:
        print("\nUntil next time, human!")

guessing_game()
