from rock_paper_scissors import rock_paper_scissors
from test import test
from test_speed import typing_speed_test
while True:
    print("-----------------Please choose game-----------------")
    print("1. Rock, paper, scissors;\n 2. Typing speed test game;\n 3. Test game;\n 4. Exit")
    choose = int(input("Choose game by numbers: "))
    if choose == 1:
        rock_paper_scissors()
    elif choose == 2:
        typing_speed_test()
    elif choose == 3:
        test()
    else:
        break