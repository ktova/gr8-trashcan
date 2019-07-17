import Game
import Depot
from Depot import rouletteCases
from Depot import list_of_cases
from Depot import Case

class Gamble:
#Function for the ending gamble part
    pxmisebet = 0


    def colorpicker(self):
        """Gamble on colors"""
        colors = {
            "red": "Red",
            "black": "Black"
        }
        print("What color do you want to gamble on ? [ red | black ]")
        pxcolor = input().lower()
        try:
            print(f"How many tokens do you want to gamble on {colors[pxcolor]} ?")
            pxmisebet = input()
            return pxmisebet
        except:
            print("Error, that's not a valid color")

#Gamble on odd/even
