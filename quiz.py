print("A very warm welcome to the General Knowledge Quiz!")
answer_user = input("Do you want to start? (yes/no): ")

if  answer_user.lower() == "yes":
    print("Great! Let's get started!")
elif answer_user.lower() == "no":
    print("OK! See you next time!")
else:
    print("Invalid response! Please answer with 'yes' or 'no'.")

print("Question 1: What is the capital of France?" "\n (A) Paris" "\n (B) London" "\n (C) Berlin" "\n (D) Madrid")
answer1 = input("Enter the letter corresponding to your answer: ")

if answer1.lower() == "a":
    print("Congratulations! You got it right!")
else:
    print("Incorrect answer! The correct answer is (A) Paris.")


