import os
import time
import random


from hangman.draws import draw # in this file are los "Draws" the game


class Hangman:
    cant_lives = 7
    intents = 0
    underscore = "_"
    found_letters = 0
    char_user = ""
    want_play = True

    def __init__(self):
        self.chosen_word = self.choose_word() # We execute the function Choose_word() for chosen the word to play
        self.sentence = self.chosen_word[0]
        self.secret_word = self.chosen_word[1]
        translate_word = self.sentence.maketrans('ÁÉÍÓÚ', 'AEIOU')
        self.new_sentence= self.sentence.translate(translate_word)  

    def ask_for_exit(self):
        again = input("Do you want to play again? Y/n: ").upper()

        if again == "Y":
            os.system("cls")
            Hangman().run()

        print("\nಠ_ಠ, 😁 Thanks for playing, come back soon!! 👋👋 \n")
        self.want_play = False
        exit()       
    

    def request_character(self):
        try:
            self.char_user = input("\nEnter a letter: ").upper()
            if len(self.char_user) <= 0:
                self.char_user = input("Enter a letter: ").upper()
            os.system("cls")
        except AssertionError as ae:
            print(ae)
        return None


    def start(self):
        """ Here are the main functions of the game """ 
        draw(self, self.cant_lives)

        print("Number lives:", self.cant_lives)
        print('\n', ''.join(self.secret_word), '\n')

        self.request_character()


        """ We compare the letter that the player enters with the letters found and with the blank spaces
         to determine if it has already been found, is new or does not exist within the secret word """
        while self.want_play:
            for i in range(len(self.new_sentence)):
                if self.char_user == self.secret_word[i]:
                    print("\nThis letter has already been found\n")
                    self.intents = 1 # We determine that the word entered this, so as not to lose lives.  
                    time.sleep(3)
                    break
                elif self.underscore == self.secret_word[i]:
                    char = self.new_sentence[i]
                    if self.char_user == char:
                        self.secret_word[i] = self.char_user
                        self.intents = 1
                        self.found_letters +=1 # When we find a letter add us to one to know when the word is complete 
            
            # If there are no attempts, a life is lost
            if self.intents == 0:
                self.cant_lives -= 1      

            os.system("cls")

            draw(self, self.cant_lives)
            print("Number lives:", self.cant_lives)
            print("\n", ''.join(self.secret_word))

            self.intents = 0

            if self.found_letters == len(self.sentence):
                os.system("cls")
                draw(self, 10)
                print("\n(☞ﾟヮﾟ)☞ 🏆 YOUR WIN!! 🏆 ☜(ﾟヮﾟ☜)  ( •_•)>⌐■-■  (⌐■_■).... \n")
                print(f"The secret word was: {self.sentence}\n")
                
                self.ask_for_exit()
                
            if self.cant_lives <= 0:
                print("\nYour Lose!!! (╯°□°）╯ (┬┬﹏┬┬)\n")
                print(f"The secret word was: {self.sentence}\n")

                self.ask_for_exit()

            self.request_character()


    def choose_word(self):
        """ In this function a random word is chosen to play """
        word_play = []
        options_of_words = []

        # Open the file where is our words to play
        with open("./archivos/datos.txt", "r", encoding="utf-8") as file:
            for option in file:
                options_of_words.append(option.strip().upper())

        random_option = random.choice(options_of_words) # Chosen random word
        word_play.append(random_option)


        # We change the letters for underscores
        secret_word = ['_' for word in random_option]
        word_play.append(secret_word)

        # We send the information with which we will play 
        return word_play 


    def run(self):
        """ In this function we start the game """
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

        try:
            tecla = str(ord(input("Hit G and Enter to continue ")))
            assert tecla == "71" or tecla == "103" or len(tecla) == 0, "-----------YOU CAN ONLY ENTER LETTER G-----------"
            
            print("\n'G' of Game")
            time.sleep(2.5)

            os.system("cls")
            self.start()

        except AssertionError as ae:
            os.system("cls")
            print(ae)
            self.run()
        except TypeError as te:
            os.system("cls")
            print("-----------Start wiht letter G and Enter-----------")
            self.run()

        return None
