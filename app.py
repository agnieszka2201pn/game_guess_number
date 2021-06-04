from random import randint

def draw_number(a=1, b=101):
# """
# function provides randomly chosen number
# """
    return randint(a, b)

def check_results():
# """
# function provides users input, check if it's valid and compares it to the number chosen by computer.
# """

    drawn_number = draw_number()

    while True:
        user_input = input("Guess the number: ")
        try:
            user_input_int = int(user_input)
        except ValueError:
            return "It is not a number"

        if user_input_int > drawn_number:
            print("Too big")
        elif user_input_int < drawn_number:
            print("Too small")
        else:
            return "You win!"


print(check_results())
