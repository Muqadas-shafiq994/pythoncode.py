import random
import string

def guess_the_alphabet():
    print("welcome to Alphabet guessing game!:")
   
    secret_letter=random.choice(string.ascii_letters)
    attempt=0
    max_attempts= 6
    while attempt<max_attempts:
        guess=input(f"Attempt{attempt+1}.Guess a Alphabet from a to z  or A to Z:")
        attempt+=1
        if len(guess)!=1 or guess is not string.ascii_letter:
            print("please enter a alphabet from a to z")
        
    if guess<secret_letter:
        print("Too low in the alphabet.Try again:")
    elif guess> secret_letter:
        print("Too high in the alphabet. Try again")
    else:
        print(f" Congratulations! You guessed it right in {attempt} attempts")
    if guess != secret_letter:
        print(f"your guess is invalid . Not from alphabet!") 

guess_the_alphabet() 
         
       