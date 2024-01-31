from random import randint
# import sys

def run_guess(guess, answer):
    if guess > 0 and guess < 11:  # the code can be simplified: if 0 < int(guess) < 11:
        if guess == answer:
            print("You're a genius!")
            return True
    else:
        print("Hey, Bozo, I said 1-10.")

# answer = randint(int(sys.argv[1]),int(sys.argv[2]))
if __name__ == "__main__":
    answer = randint(1,10)
    while True:
        try:
            guess = int(input("Guess a number 1-10: "))
            if (run_guess(guess,answer)):
                break
        except ValueError:
            print("Please enter a number. ")
            continue

