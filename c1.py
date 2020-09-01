# Write a program that takes a users input, if the input is a number,
# print if the number is even or odd, if it is not a number,
# count how long the string is and print if it is even or odd.

# this program will only run on Python 3.8 and above!

import random
import requests

class challenge1():
    def __init__(self, userInput):
        self.userInput = userInput

    def _actualing(self, number):
        return 'odd' if number % 2 == 1 else 'even'

    def _numericalnessQuestionMark(self):
        if isinstance(self.userInput, str) and not self._canNumerical():
            self.isInputTypeNum = False
            return len(self.userInput)
        if isinstance(self.userInput, int):
            self.isInputTypeNum = True
            return self.userInput
        if isinstance(self.userInput, float):
            # https://www.geeksforgeeks.org/check-whether-given-floating-point-number-even-odd/
            self.isInputTypeNum = True
            dotSeen = False
            for i in range(len((s := str(self.userInput)))-1, -1, -1):
                if (s[i] == '0' and dotSeen == False): continue
                if (s[i] == '.'): dotSeen = True; continue
                return int(s[i])
        raise Exception('user input is not a string, integer or float')
    
    def _canNumerical(self):
        try: self.userInput = float(self.userInput)
        except: return False
        return True

    def __str__(self):
        numerical = self._numericalnessQuestionMark()
        result = self._actualing(numerical)
        output = f"number {self.userInput} is" if self.isInputTypeNum else f"string is {numerical} characters long and is"
        return f'The given {output} {result}'

def getDefaultInput():
    '''
        OUTPUT: returns either a random number or a random string

        number - generated using random, by truncating the "0."
        string - pulled from random-word-api.herokuapp.com
    '''

    # randomly choose if the default input will either be a number or string
    if bool(int(random.random()*10%2)):
        # default input will be a number
        return int(str(random.random())[2:])
    else:
        # default input will be a string
        if (response := requests.get('https://random-word-api.herokuapp.com/word')).status_code == 200:
            return response.json()[0]
    return 'error'

if __name__ == "__main__":
    userInput = defaultInput if (userInput := input(f'Need Input [Press Enter to use {(defaultInput := getDefaultInput())}]:')) == "" else userInput
    print(f'Your input: {userInput}')
    print(challenge1(userInput))
