"""
rock paper Scissors game
"""


option = input("Do you want to Start the game(Yes/y or No/n):")
is_want = False     #if user want to continue the game or not
is_find = False     #this will be used to exti from the main loop

while not is_find:
    if option == 'Yes' or option == 'yes' or option == 'y' or option == 'Y':
        is_want = True
        is_find = True

        while is_want:
            player1 = input("Player1, Enter you value for 'Rock' press r or R"
                            "; For 'Scissors' press s or S,"
                            "; For'Paper' press p or P ")
            p1_val = ""
            if player1 == 'r' or player1 == 'R':
                p1_val = 'r'
            elif player1 == 'p' or player1 == 'P':
                p1_val = 'p'
            elif player1 == 's' or player1 == 'S':
                p1_val = 's'
            else:
                print("Enter the correct value")
                continue

            player2 = input("Player2, Enter you value for 'Rock' press r or R"
                            "; For 'Scissors' press s or S,"
                            "; For'Paper' press p or P ")

            p2_val = ""
            if player2 == 'r' or player2 == 'R':
                p2_val = 'r'
            elif player2 == 'p' or player2 == 'P':
                p2_val = 'p'
            elif player2 == 's' or player2 == 'S':
                p2_val = 's'
            else:
                print("Enter the correct value")
                continue

            if ((p1_val == 'r' and p2_val == 's') or (p1_val == 's' and p2_val == 'p') or (p1_val == 'p' and p2_val == 'r')):
                print("\nPlayer1 Wins\n")
            else:
                print("\nPlayer2 Wins\n")

            option = input("Do you want to Start the game(Yes/y or No/n):")
            if option == 'Yes' or option == 'yes' or option == 'y' or option == 'Y':
                is_want = True
                is_find = True
            elif option == 'No' or option == 'no' or option == 'n' or option == 'n':
                is_want = False;
                is_find = True
            else:
                print("Please, answer in Yes/y/Y or No/n/N")
                print("Game ended")
                is_find = False

    elif option == 'No' or option == 'no' or option == 'n' or option == 'n':
        is_want = False;
        print("Game ended")
        is_find = True
    else:
        print("Please, answer in Yes/y/Y or No/n/N")
        option = input("Do you want to Start the game(Yes/y or No/n):")
        is_find = False
