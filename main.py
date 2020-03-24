# This program is similar to the terminal hacking system introduced in Fallout 4.
#
# The computer chooses a random password which you have to guess within 4 attempts.
# Every time you guess wrong you will be presented with the amount of shared letters
# between the password you tried to enter and the password the computer chose.
# If you fail after 4 attempts, the terminal will lock you out and you will have
# to start again with a new password chosen by the computer and new words to choose
# from.
#
# Think carefully! :)

import random

class TerminalPassword:

    def __init__(self):
        self.possibleWords = [ 'text', 'leaf', 'over', 'dash', 'true', 'pipe', 'ball', 'glad', 'back', 'jail', 'moon',
                          'quit', 'star', 'full', 'dull', 'shut', 'vent', 'mesh', 'evil', 'vest', 'wool', 'twit',
                          'mitt', 'wilt', 'word', 'ward', 'wood', 'flex', 'axis', 'yell', 'troy', 'girl', 'tilt',
                          'xray', 'fuzz', 'fuze', 'maze', 'quiz' ]
        self.possiblePasswords = self.setPossiblePasswords
        self.currentPassword = self.setRandomPassword()
        self.maxAttempts = 4
        self.triedAttempts = 0
        self.startGame()
        startOver = self.shouldStartOver()
        while startOver == True:
            self.startGame()
            startOver = self.shouldStartOver()

    def shouldStartOver(self):
        startOver = input("Do you wish to try again? (Y / N): ")
        if startOver == "Yes" or startOver == "yes" or startOver == "Y" or startOver == "y":
            self.triedAttempts = 0
            return True
        else:
            return False


    @property
    def setPossiblePasswords(self):
        tempList = [None] * 10
        for x in range(10):
            randomIndex = random.randrange(0, len(self.possibleWords)-1)
            while self.possibleWords[randomIndex] in tempList:
                randomIndex = random.randrange(0, len(self.possibleWords) - 1)
            tempList[x] = self.possibleWords[randomIndex]
        return tempList

    def setRandomPassword(self):
        return self.possiblePasswords[random.randrange(0, len(self.possiblePasswords)-1)]

    def startGame(self):
        print("The computer has chosen a password which is displayed below along with others.\n"
              "You have %d attempts to guess the right password.\n"
              "Each time you guess a password, you will be notifyed how many letters are shared by the computer's password"
              % self.maxAttempts)
        for i in range(1, len(self.possiblePasswords), 2):
            print("%d. %s\t\t%d. %s" % (i, self.possiblePasswords[i-1], i+1, self.possiblePasswords[i]))
        won = self.checkUserGuess()
        while won == False:
            won = self.checkUserGuess()

    # Validation method - only allow integers
    def allowOnlyInt(self, input):
        try:
            temp = int(input)
            return temp
        except:
            return -1

    def checkSharedLettersAmount(self, guessedPassword):
        temp = self.currentPassword
        for i in range(len(guessedPassword)):
            if guessedPassword[i] in temp:
                temp = temp.replace(guessedPassword[i], '')
        return len(guessedPassword) - len(temp)

    def checkUserGuess(self):
        if self.triedAttempts >= self.maxAttempts:
            print("The terminal has locked you out...\nExiting...")
            return True
        userGuessInput = self.allowOnlyInt(input("Please enter a number to see if that is the password: "))
        self.triedAttempts += 1
        if userGuessInput == -1:
            return False
        while userGuessInput == -1 or userGuessInput < 1 or userGuessInput > 10:
            userGuessInput = self.allowOnlyInt(input("Please enter a valid number: "))
        if self.currentPassword != self.possiblePasswords[userGuessInput-1]:
            print("The amount of letters shared is %d" % self.checkSharedLettersAmount(self.possiblePasswords[userGuessInput-1]))
            return False
        else:
            print("The password is correct! Congratulations")
            return True

def main():
    terminal = TerminalPassword()

if __name__ == "__main__":
    main()