import random

name = input("Enter your name please:   ")

while True:
    question = "Would you like to know if you will win the lottery? (yes/no) "
    answer = input(question)

    if answer.lower() == 'no':
        print("Goodbye!")
        break
    elif answer.lower() == 'yes':
        break
    else:
        print("Please answer 'yes' or 'no'.")

question = "Will I win the lottery?"
answer = ""

random_number = random.randint(1, 10)

if random_number == 1:
    answer = "Yes - definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
elif random_number == 10:
    answer = "Signs point to yes"
else:
    answer = "Error"

if name == "":
    print("Question: " + question + '\n' + answer)
else:
    print(name + " asks: " + question + '\n' + answer)
