"""You, the user, will have in your head a number between 0 and 100. 
The program will guess a number, and you, the user, 
will say whether it is too high, too low, or your number."""

#TO DO
# implement a binary search

class GuessNumber:

    guesses = 0

    def __init__(self, number, mn=0, mx=100):
        self.number = number
        self.min = mn
        self.max = mx
        self.guess = 0

    def get_guess(self):
        self.guess = input(f"Please guess a number ({self.min} - {self.max}): ")

        if self.valid_number(self.guess):
            return int(self.guess)
        else:
            print("Please enter a valid number.")
            return self.get_guess()

    def valid_number(self, str_number):
        try:
            number = int(str_number)
        except:
            return False
        return self.min <= number <= self.max
    
    def play(self):
        while True:
            self.guesses += 1
            guess = self.get_guess()
            if guess < self.number:
                print("You guess was under.")
            elif guess > self.number:
                print("Your guess was over.")
            else: # number guessed
                print("You guessed a number!")
                break

        print(f"You guessed it in {self.guesses} guesses.")


game = GuessNumber(223,0,1000)
game.play()
