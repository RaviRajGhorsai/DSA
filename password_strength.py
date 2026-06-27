"""


"""

def get_num_guesses(length: int) -> int:
    total_guess = 0

    for i in range(length):
        total_guess += 26 ** (i+1)

    return total_guess
