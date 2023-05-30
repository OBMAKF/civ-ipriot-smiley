from sense_hat import SenseHat


class Smiley:
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)
    BLANK = (0, 0, 0)

    def __init__(self, complexion: tuple[int, int, int] = YELLOW):
        # We have encapsulated the SenseHat object
        self.sense_hat = SenseHat()
        self.my_complexion = complexion
        
        I = complexion
        O = self.BLANK
        self.pixels = [
            O, I, I, I, I, I, I, O,
            I, I, I, I, I, I, I, I,
            I, I, I, I, I, I, I, I,
            I, I, I, I, I, I, I, I,
            I, I, I, I, I, I, I, I,
            I, I, I, I, I, I, I, I,
            I, I, I, I, I, I, I, I,
            O, I, I, I, I, I, I, O,
        ]
    
    def complexion(self) -> tuple[int, int, int]:
        """
        Retrieve the base colour(complexion) for the smiley
        as an (R,G,B) tuple, default as yellow.
        :returns: (R,G,B) value
        :rtype tuple[int, int, int]:
        """
        return self.my_complexion

    def dim_display(self, dimmed=True):
        """
        Set the SenseHat's light intensity to low (True) or high (False)
        :param dimmed: Dim the display if True, otherwise don't dim
        """
        self.sense_hat.low_light = dimmed

    def show(self):
        """
        Show the smiley on the screen.
        """
        self.sense_hat.set_pixels(self.pixels)
