import time
import random

def mistake(partest, usertest):
    error = 0
    for i in range(min(len(partest), len(usertest))):
        if partest[i] != usertest[i]:
            error += 1
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(userinput) / time_R
    return round(speed, 2)

if __name__ == '__main__':
    test_sentences = [
        "A Python speed test project typically involves measuring the execution time of a specific piece of code or a function.",
        "You can achieve this using Python's built-in time module.",
        "Here's a simple example of a Python speed test project."
    ]

    while True:
        ck = input("Ready to test? (yes/no): ")
        if ck.lower() == "yes":
            test1 = random.choice(test_sentences)
            print("\n**** Typing speed test ****")
            print(test1)
            print("\nType the above sentence:")
            input("Press Enter to start...")
            time_1 = time.time()
            testinput = input("Enter: ")
            time_2 = time.time()

            print("\nSpeed: {} w/sec".format(speed_time(time_1, time_2, testinput)))
            print("Errors: ", mistake(test1, testinput))
        elif ck.lower() == 'no':
            print("Thank you!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

### GUI
root = tk.Tk()
root.title("Typing Speed Test")

test_sentences = [
    "A Python speed test project typically involves measuring the execution time of a specific piece of code or a function.",
    "You can achieve this using Python's built-in time module.",
    "Here's a simple example of a Python speed test project."
]

test_label = tk.Label(root, text="", wraplength=400)
test_label.pack(pady=10)

input_text = tk.Entry(root, width=50)
input_text.pack()

submit_button = tk.Button(root, text="Submit", command=start_typing_test)
submit_button.pack(pady=10)

start_typing_test()

root.mainloop()


