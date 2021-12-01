import time

from hangman.hangman import Hangman

def start_game():
    """ Start the game """  
    hangman.run()

if __name__ == "__main__":
    hangman = Hangman()
    try:
        start_game()
    except KeyboardInterrupt as e:
        print("\n\nForced closure CTRL + C\nBye!!", e)
        time.sleep(2.5)
        exit()
   