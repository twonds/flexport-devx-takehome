import random


def rock_paper_scissors(user_choice: int) -> int:
    """
    A Simple rock, paper scissors game.
    """
    # Generate computer choice
    pc_choice = random.randint(0, 2)
    if pc_choice == user_choice:
        return 0, pc_choice
    elif (user_choice + 1) % 3 == pc_choice % 3:
        return -1, pc_choice
    else:
        return 1, pc_choice
