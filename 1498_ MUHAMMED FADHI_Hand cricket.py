import random

def toss(l):
    # Simulate a coin toss
    return [1, True] if random.randint(0, 1) == l else [2, False]

def game(username):
    score = 0
    l = int(input("Call for toss! Press 0 for head and 1 for tail: "))
    batting, user_bats_first = toss(l)
    print(f"{username} bat first" if user_bats_first else "Computer bats first")

    while True:
        try:
            g = random.randint(1, 6)
            u = int(input("Enter a number between 1 and 6: "))
            if u < 1 or u > 6:
                raise ValueError
            print("Computer entered", g)
            if u == g:
                print(f"{username} are out!")
                batround(score + 1, 1 if batting == 2 else 0, username)
                break
            else:
                score += u if batting == 1 else g
                print(f"{username}'s score is", score) if batting == 1 else print("Computer's score is", score)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")

def batround(target, who, username):
    score = 0
    while target > 0:
        try:
            g = random.randint(1, 6)
            u = int(input("Enter a number between 1 and 6: "))
            if u < 1 or u > 6:
                raise ValueError
            print("Computer entered", g)
            if u == g:
                print(f"{username} are out!" if who else "Computer is out!")
                print("Remaining target is", target)
                break
            elif who:
                target -= u
                score += u
                print(f"{username}'s score is", score)
            else:
                target -= g
                print("Computer's score is", target)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
    if who:
        print(f"{username} won the match!" if target <= 0 else "Computer won the match!")
    else:
        print("Computer won the match!" if target <= 0 else f"{username} won the match!")

def check():
    while True:
        c = input("Enter y to play again, n to quit: ").strip()
        if c == 'y':
            username = input("Enter your name: ")
            game(username)
        elif c == 'n':
            print("Thank you for playing!")
            quit()
        else:
            print("Invalid input. Please enter y or n.")

username = input("Enter your name: ")
game(username)
check()