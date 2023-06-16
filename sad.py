from smiley import Smiley
from blinkable import Blinkable
from time import sleep


class Sad(Smiley, Blinkable):
    def __init__(self) -> None:
        super().__init__(complexion=self.BLUE)

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self) -> None:
        """
        Method that draws the mouth on the standard faceless smiley.
        """
        mouth = [49, 54, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open: bool = True) -> None:
        """
        Method that draws the eyes (open or closed) on the standard smiley.
        :param wide_open: True if eyes opened, False otherwise
        """
        eyes = [10, 13, 18, 21]
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK if wide_open else self.complexion()
    
    def blink(self, delay: float = 0.25) -> None:
        self.draw_eyes(wide_open=False)
        self.show()
        sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()
