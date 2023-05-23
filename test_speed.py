import time

def typing_speed_test():
    print("------- Welcome to the Typing Speed Test! -------")
    print("Type the following sentence as quickly and accurately as possible:")
    print("\n'The quick brown fox jumps over the lazy dog.'\n")

    input("Press Enter to start...")
    start_time = time.time()

    sentence = "The quick brown fox jumps over the lazy dog."
    user_input = input("> ")

    end_time = time.time()
    elapsed_time = end_time - start_time

    words = sentence.split()
    num_words = len(words)
    user_words = user_input.split()
    num_user_words = len(user_words)

    correct_words = 0
    for i in range(num_user_words):
        if i >= num_words:
            break
        if user_words[i] == words[i]:
            correct_words += 1

    accuracy = correct_words / num_words * 100
    wpm = num_user_words / elapsed_time * 60 / 5

    print(f"\nYou typed {num_user_words} words in {elapsed_time:.2f} seconds.")
    print(f"Your typing speed is {wpm:.2f} words per minute.")
    print(f"Your accuracy is {accuracy:.2f}%.")
