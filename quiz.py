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


while answer1.lower() != "a":
    print("Question 1: What is the capital of France?" "\n (A) Paris" "\n (B) London" "\n (C) Berlin" "\n (D) Madrid")
    answer1 = input("Enter the letter corresponding to your answer: ")

    if answer1.lower() == "a":
        print("Congratulations! You got it right!")
    else:
        print("Incorrect answer again! The correct answer is (A) Paris.")


print("Question 1: What is the capital of France?" "\n (A) Paris" "\n (B) London" "\n (C) Berlin" "\n (D) Madrid")
answer2 = input("Enter the letter corresponding to your answer: ")

attempts = 0

while answer2.lower() != "a" and attempts < 3:
    print("Question 1: What is the capital of France?" "\n (A) Paris" "\n (B) London" "\n (C) Berlin" "\n (D) Madrid")
    answer2 = input("Enter the letter corresponding to your answer: ")
    attempts += 1

    if answer2.lower() == "a":
        print("Congratulations! You got it right again!")
        break
    else:
        print(f"Incorrect answer! You have {3 - attempts} attempts left.")


