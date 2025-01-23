"""
Are-You-A-Spy problem:
Channing Moor - January 2025
"""

def main() -> None:
    # Get/setup greeting and response
    grset: str = input()
    grset = grset.lower()
    greeting,response = grset.split("|")

    # Get rid of non alphabetic characters
    newresponse: str = 
    for i in range(len(response)):
        if response[i].isalpha() == False:
            response.replace(response[i], "")

    # Setup bool and check for anagram
    for ch in response:
        # If it is not a letter
        elif ch not in greeting:
            print("You're not a secret agent!")
        else:
            spy = False
            break
    
    print("That's my secret contact!")


if __name__ == "__main__":
    main()  

