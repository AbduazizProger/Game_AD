def test():
    while True:
        print("------- Some tests are here try to solve them -------\n")
        questions = {
            "What kind of loops are there in Python: ": ["for, do...whlie, while", "only while", "only for", "for and while"],
            "What does print function do: ": ["Prints some text using printers", "Gets input", "Prints some text in console", "There is no this kind of function"],
            "Which are data types from python here: ": ["int, float, double, String", "str, int, float", "pointers, null, functions", "Aray, Map"],
            "Is python compiling language: ": ["yes", "no", "I don't know", "Yes and no😂"],
            "how you can create a variable in Python: ": ["<name> = <value>", "<data-type> <name>", "var <name>", "let <name>"],
        }

        trues = [4, 3, 2, 2, 1]
        istrue = []
        j = 0
        for question, answers in questions.items():
            j += 1
            print(question)
            i = 0
            for answer in answers:
                i += 1
                print(f"{i}){answer}")
            some = int(input("Please answer by numbers: "))
            if some == trues[j - 1]:
                print("You are right!")
                istrue.append(True)
            else:
                print("You are wrong!")
                istrue.append(False)
        rights = 0
        wrongs = 0
        for answer in istrue:
            if answer:
                rights += 1
            else:
                wrongs += 1
        print(f"You have {rights} number of right answers and {wrongs} of wrongs")
        replay = input("Will you try again (y/n)")
        if replay == "n":
            return;
