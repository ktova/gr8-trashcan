cword = ["cobra", "cacao", "cocaine", "cannes", "cannabise", "camus"]
sword = "cannabis"

Bannounce = "We added a little welcome bonus, here is your new starting Credits :"

#List of every playable numbers from the roulette - equivalent de .append x dans roulettecases
rouletteCases = [
    x for x in range(0, 37)
]
#Bonuses value
bonuses = [2, 1.625, 1.5, 1.625, 1.75]

#colss
f1 = (1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34)
f2 = (2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35)
f3 = (3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36)

#dozens
d1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
d2 = (13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)
d3 = (25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36)

#rows
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]
l4 = [10, 11, 12]
l5 = [13, 14, 15]
l6 = [16, 17, 18]
l7 = [19, 20, 21]
l8 = [22, 23, 24]
l9 = [25, 26, 27]
l10 = [28, 29, 30]
l11 = [31, 32, 33]
l12 = [34, 35, 36]

class Case:
    """Cases properties"""

    number = 0
    d = 1

    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return "Case()"

    def color(self):
        """Define number's color"""
        if self.number == 0:
            return 0
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
            return 0
        else:
            result_of_division = self.number % 3
            if result_of_division == 0:
                return 3
            else:
                return result_of_division

    def is_even(self):
        """Define if number is odd or even"""
        return self.number % 2 == 0

    def dozens(self):
        """Define number's row"""
        if self.number == 0:
            return 0
        elif self.number >= 1 and self.number <= 12:
            return 1
        elif self.number >= 13 and self.number <= 24:
            return 2
        elif self.number >= 25 and self.number <= 36:
            return 3


#list_of_cases = [Case(x) for x in range(0, 37)]

#print(Case(0).column())

