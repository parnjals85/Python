questions = (("Bharat ka Rashtrapati kaun hai?: "),
            ("Bharat ki Rajdhani kya hai?: "),
            ("Taj Mahal kis shehar me hai?: "),
            ("Bharat ka Rashtriya Pashu kaunsa hai?: "),
            ("Bharat ka Rashtriya Pakshi kaunsa hai?: "),
            ("Computer ka Father kaun mana jata hai?:"),
            ("Olympic Games kitne saal me hote hain?:"),
            ("World ka sabse bada samundar kaunsa hai?:"),
            ("Bharat ka Rashtriya Phool kaunsa hai?:"),
            ("Red Planet kis planet ko kehte hain?:"))

options = (("A. Narendra Modi" , "B. Droupadi Murmu" , "C. Amit Shah" , "D. Ram Nath Kovind"),
           ("A. Mumbai" , "B. Kolkata" , "C. Delhi" , "D. Chennai"),
           ("A. Delhi" , "B. Jaipur" , "C. Agra" , "D. Lucknow"),
           ("A. Lion" , "B. Elephent" , "C. Tiger" , "D. Leopard"),
           ("A. Sparow" , "B. Peacock" , "C. Eagle" , "D. Crow"),
           ("A. Bill Gates" , "B. Steve Jobs" , "C. Charles Babbage" , "D. Alan Turning"),
           ("A. 2 Saal" , "B. 3 Saal" , "C. 4 Saal" , "D. 5 Saal"),
           ("A. Atlantic" , "B. Indian Ocean" , "C. Arctic Ocean" , "D. Pacific Ocean"),
           ("A. Rose" , "B. Sunflower" , "C. Lotus" , "D. Lily"),
           ("A. Venus" , "B. Mars" , "C. Jupitar" , "D. Satuurn"))

answers = ("B","C","C","C","B","C","D","D","C","B");
guesses = []
score = ()
question_num = 0

for question in questions:
    print("------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter the (A.B.C.D:): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+=1
        print("!Correct")
    else:
        print("!incorrect")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
 
    print("---------")
    print(" Results ")
    print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
