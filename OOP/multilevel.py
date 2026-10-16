class Factory:
    def __init__(self,pocket,zip):
        self.pocket = pocket
        self.zip = zip


class PuneFactory(Factory):
    def __init__(self, pocket, zip,color):
        super().__init__(pocket, zip)
        self.color = color

class MumbaiFactory(PuneFactory):
    def __init__(self, pocket, zip, color,bag):
        super().__init__(pocket, zip, color)
        self.bag = bag


obj = MumbaiFactory()