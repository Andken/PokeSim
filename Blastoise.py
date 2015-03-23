import CardTypes

class Blastoise(CardTypes.Pokemon):
    def play(self):
        assert "play: " + self.name()

    def name(self):
        return "Blastoise"

    def isWaterType(self):
        return True

