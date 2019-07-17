cword = ["cobra", "cacao", "cocaine", "cannes", "cannabise", "camus"]
sword = "cannabis"

Bannounce = "We added a little welcome bonus, here is your new starting Credits :"

#List of every playable numbers from the roulette - equivalent de .append x dans roulettecases
rouletteCases = [
    x for x in range(0, 37)
]
#Bonuses value
bonuses = [2, 1.625, 1.5, 1.625, 1.75]

class Case:
    """Cases properties"""

    number = 0

    def __init__(self, number):
        self.number = number

    def color(self):
        """Define number's color"""
        if self.number == 0:
            return None
        elif (self.number >= 1 and self.number <= 10) or (
            self.number >= 19 and self.number <= 28
        ):
            if self.number % 2 == 0:
                return "black"
            else:
                return "red"
        elif (
            self.number >= 11
            and self.number <= 18
            or (self.number >= 29 and self.number <= 36)
        ):
            if self.number % 2 == 0:
                return "red"
            else:
                return "black"



    def column(self):
        """Define number's column"""
        if self.number == 0:
            return None
        else:
            result_of_division = self.number % 3
            if result_of_division == 0:
                return 3
            else:
                return result_of_division

    def is_even(self):
        """Define if number is odd or even"""
        return self.number % 2 == 0

    def row(self):
        """Define number's row"""
        if self.number == 0:
            return None
        elif self.number >= 1 and self.number <= 12:
            return 1
        elif self.number >= 13 and self.number <= 24:
            return 2
        elif self.number >= 25 and self.number <= 36:
            return 3

list_of_cases = [Case(x) for x in range(0, 37)]
