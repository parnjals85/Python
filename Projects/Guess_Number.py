import random

number = random.randint(1,5)
while True :

   guess = int(input("Please enter the Number : "));

   if guess == number:
    print(f"Hurray! You Guessed It right the Right Number is {number}");
    break
   else:
    print(f"!Oops Not Right the Correct Number is {number}");