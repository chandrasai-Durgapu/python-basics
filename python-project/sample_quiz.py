print("Sample Quiz")
counter = 0
playing = input("Do you want to play? ")

if playing.lower() == "yes":
    print("Quiz begins! (Type 'quit' anytime to exit)\n")
    
    answer = input("What does CPU stand for? ")
    if answer.lower() == "quit":
        print("Quiz exited.")
        quit()
    elif answer.lower() == "central processing unit":
        print("Correct answer!")
        counter += 1
    else:
        print("Incorrect answer.")

    answer = input("What does RAM stand for? ")
    if answer.lower() == "quit":
        print("Quiz exited.")
        quit()
    elif answer.lower() == "random access memory":
        print("Correct answer!")
        counter += 1
    else:
        print("Incorrect answer.")

    print(f"\nYou got {counter} correct answer(s).")
else:
    print("Quitting...")
    quit()

