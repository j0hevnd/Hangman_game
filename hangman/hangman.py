import os
import time
import random

from hangman.draws import draw # in this function are "Draws" the game


class Hangman:
    __underscore = "_"
    _want_play = True

    def __init__(self):
        self.__cant_lives = 7
        
        # Execute the function pick_word() for chosen the word to play
        self.chosen_word = self.pick_word() 
        self.sentence = self.chosen_word[0]
        self.secret_word = self.chosen_word[1]
        translate_word = self.sentence.maketrans('ÁÉÍÓÚ', 'AEIOU')
        self.new_sentence = self.sentence.translate(translate_word)
        # print(self.new_sentence) # If you have a good eye see the word hahaha

    def ask_for_exit(self):
        """End the game in case the user doesn't want to continue"""
        again = input("Do you want to play again? Y/n: ").upper()

        if again == "Y":
            os.system("cls")
            Hangman().run()

        print("\nಠ_ಠ, 😁 Thanks for playing, come back soon!! 👋👋 \n")
        self._want_play = False
        exit()       
    

    def request_character(self):
        """ Request a word
        Returns: word entered
        """
        def _valid_numeric(char):
            """Validate the word entered

            Args:
                char (str): word entered for user

            Returns:
                [bool]: False if it's an invalid word, otherwise True 
            """
            if char.isnumeric(): 
                print("Don't enter numbers\n")
                return False
            
            if len(char) < 1 or len(char) > 1:
                print("Please enter only one letter\n")
                return False
            
            return True
        
        char_user = input("\nEnter a letter: ").upper()
        
        while not _valid_numeric(char_user):
            char_user = input("Enter a letter: ").upper()
    
        return char_user
    
    
    def pick_word(self):
        """ Pick a random word to play """
        options_of_words = []

        # Open the file where is our words to play
        with open("./archivos/datos.txt", "r", encoding="utf-8") as file:
            for option in file:
                options_of_words.append(option.strip().upper())

        random_option = random.choice(options_of_words) # Chosen random word

        # We change the letters for underscores
        secret_word = ['_' for _ in random_option]

        # We send the information with which we will play 
        return random_option, secret_word


    def start(self):
        """Start the game"""
        found_letters = 0
        
        def _draw_lives_and_word(lifes=None):
            """ Shows the pictures in the game, the number of lives and the underscores with a secret word
            Args:
                lifes (int, optional): In case of winning, show the picture correspondent 
                Defaults to None
            Return: None
            """
            os.system('cls')
            if lifes:
                draw(lifes)
            else:
                draw(self.__cant_lives)
            print("Number lives:", self.__cant_lives)
            print('\n', ' '.join(self.secret_word), '\n')
            
            
        def win_or_lose(intents, found_letters):
            """
            Determine if a player wins or loses
            Args:
                intents (int): 1 or 0, determines if a game life is lost
                found_letters: Number of words found
            Return: None
            """
            # If there are no attempts, a life is lost
            if intents == 0: self.__cant_lives -= 1
            
            if self.__cant_lives <= 0:
                _draw_lives_and_word()
                print("\nYour Lose!!! (╯°□°）╯ (┬┬﹏┬┬)\n")
                print(f"The secret word was: {self.sentence}\n")
                self.ask_for_exit()

            elif found_letters == len(self.sentence):
                _draw_lives_and_word(10)
                print("\n(☞ﾟヮﾟ)☞ 🏆 YOUR WIN!! 🏆 ☜(ﾟヮﾟ☜)  ( •_•)>⌐■-■  (⌐■_■).... \n")
                print(f"The secret word was: {self.sentence}\n")
                self.ask_for_exit()


        # We compare the letter that the player enters with the letters
        # found and with the blank spaces to determine if it has already 
        # been found, is new or does not exist within the secret word
        while self._want_play:
            intents = 0
            _draw_lives_and_word()
            char_user = self.request_character()
            
            for i in range(len(self.new_sentence)):
                if char_user == self.secret_word[i]:
                    print("\nThis letter has already been found\n")
                    intents = 1 # We determine that the word entered this, so as not to lose lives.  
                    time.sleep(3)
                    break
                elif self.__underscore == self.secret_word[i]:
                    char = self.new_sentence[i]
                    if char_user == char:
                        self.secret_word[i] = char_user
                        intents = 1
                        found_letters +=1 # When we find a letter add us to one to know when the word is complete 
            
            win_or_lose(intents, found_letters)


    def run(self):
        """ Game start screen """

        os.system("cls")
        def poster():   
            print("""   
||     ||       | |        ||   //||    ____      ||\ \        //||     | |       ||   //||
||     ||      //\ \       ||  // ||   / ___ \    || \ \      // ||    //\ \      ||  // ||
|||||||||     //  \ \      || //  ||  | |   | |   ||  \ \    //  ||   //  \ \     || //  ||
||     ||    //====\ \     ||//   ||  \ \___/ /   ||   \ \  //   ||  //====\ \    ||//   || 
||     ||   //      \ \    ||/    ||   \ ___ /    ||    \ \//    || //      \ \   ||/    ||
                                           /||\ 
                                         _| || |_
                                            ||
                                         \__/\__/                                     GAME
    """)
            print("!!!!!Welcome to Hangman game!!!!! \nGo to start \nGuess the word!!\n")
        
        poster()
        
        while True:
            try:
                tecla = str(ord(input("Hit G and Enter to continue ")))
                assert tecla == "71" or tecla == "103" or len(tecla) == 0, f"\n{'You only can start with letter G':-^52s}\n"
                
                print("\n'G' of Game")
                time.sleep(2.5)

                os.system("cls")
                self.start()
                break
            except AssertionError as ae:
                print(ae)
            except TypeError as te:
                print(f"\n{'Start wiht letter G and Enter':-^52s}\n")

        return None
