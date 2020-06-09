score = 0


answer1 = input("what is my name? \na. Sharuk \nb. noor \nc.ashiq \nAnswer: ")
if answer1 == "a" or answer == "Sharuk":
    score += 1
    print("correct!")
    print("score: ",score)
    print("\n")
else:
    print("Incorrect! The answer is Sharuk.")
    print("\n")



answer2 = input("what is my favoraite language? \na. clanguage  \nb. java \nc.python \nAnswer: ")
if answer2 == "c" or answer == "python":
    score += 1
    print("correct!")
    print("score: ",score)
    print("\n")
else:
    print("Incorrect! The answer is python.")
    print("\n")




answer3 = input("what is my nickname? \na. Sharuk \nb. sharu \nc.pathan \nAnswer: ")
if answer3 == "b" or answer == "Sharu":
    score += 1
    print("correct!")
    print("score: ",score)
    print("\n")
else:
    print("Incorrect! The answer is Sharu.")
    print("\n")

if score<= 1:
    print("Your total score is:",score, "-you suck!")
elif score ==2:
     print("Your total score is:",score, "-you went ok.")
else:
     print("Your total score is:",score, "-you are awesome!")
    








