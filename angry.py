from smiley import Smiley


class Angry(Smiley):
    """
    Angry is a subclass of Smiley.
    
    Displays a representation of an angry face.
    """
    def __init__(self) -> None:
        super(Smiley, self).__init__(complexion=self.RED)
        
        self.draw_eyes()
    
    def draw_eyes(self, wide_open: bool = True) -> None:
        """
        Method that draws the eyes (open or closed) on the standard smiley.
        :param wide_open: True if eyes opened, False otherwise
        """
        eyes = [17, 22, 26, 29]
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK if wide_open else self.complexion()
