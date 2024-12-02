"""
This is the High Enough Game.
You roll three dice. If the total is higher than 13, then the user wins the amount rolled.
Channing and Dwijesh - November 2024
"""
import random

def main() -> None:
    MIN_WIN: int = 13
    total: int = 0

    # roll a die 3x and add up the total
    die1: int = random.randint(1, 6)
    die2: int = random.randint(1, 6)
    die3: int = random.randint(1, 6)
    total += die1+die2+die3

    # print out the results
    print(f"{die1} + {die2} + {die3} = {total}")
    # if your total is more than MIN_WIN, you win that many dollars
    if total > MIN_WIN:
        print(f"You win ${total}!")
    # otherwise you don't win
    else:
      print("You lose.")
    

if __name__ == "__main__":
    main()