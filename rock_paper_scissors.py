import random

def rock_paper_scissors():
    while True:
        print("------- Rock(🪨 ), paper(📃), scissors(✂️ ) -------\n")

        variants = ["Rock(🪨 )", "Paper(📃)", "Scissors(✂️ )"]
        for i in range(len(variants)):
            print(f"To choose {variants[i]} input {i + 1},")

        answer = variants[int(input("Input wich one you want to choose: ")) - 1]
        computer = random.choice(variants)
        if computer == "Rock(🪨 )" and answer == "Scissors(✂️ )":
            print("Rock(🪨 ) vs Scissors(✂️ )")
            print("YOU LOSE😂😂😂")
        elif computer == "Rock(🪨 )" and answer == "Paper(📃)":
            print("Rock(🪨 ) vs Paper(📃)")
            print("YOU WIN😒😒😒")
        elif computer == "Rock(🪨 )" and answer == "Rock(🪨 )":
            print("Rock(🪨 ) vs Rock(🪨 )")
            print("Same lets try again😊😊😊")
        elif computer == "Scissors(✂️ )" and answer == "Rock(🪨 )":
            print("Scissors(✂️ ) vs Rock(🪨 )")
            print("YOU WIN😒😒😒")
        elif computer == "Scissors(✂️ )" and answer == "Paper(📃)":
            print("Scissors(✂️ ) vs Paper(📃)")
            print("YOU LOSE😂😂😂")
        elif computer == "Scissors(✂️ )" and answer == "Scissors(✂️ )":
            print("Scissors(✂️ ) vs Scissors(✂️ )")
            print("Same lets try again😊😊😊")
        elif computer == "Paper(📃)" and answer == "Rock(🪨 )":
            print("Paper(📃) vs Rock(🪨 )")
            print("YOU LOSE😂😂😂")
        elif computer == "Paper(📃)" and answer == "Scissors(✂️ )":
            print("Paper(📃) vs Scissors(✂️ )")
            print("YOU LOSE😂😂😂")
        elif computer == "Paper(📃)" and answer == "Paper(📃)":
            print("Paper(📃) vs Paper(📃)")
            print("Same lets try again😊😊😊")
        replay = input("Will you try again (y/n)")
        if replay == "n":
            return;
