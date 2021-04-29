from hangman.hangman import Hangman

def start_game():
    """ Start the game """  
    hangman.run()


if __name__ == "__main__":
    hangman = Hangman()
    
    try:
        start_game()
    except KeyboardInterrupt as ki:
        print(ki)
        finish = input("Would finish the game? Y/n: ").upper()
        if finish != "Y":
            start_game()
        exit()
   