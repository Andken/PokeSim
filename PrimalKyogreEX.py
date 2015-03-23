import CardTypes

class PrimalKyogreEX(CardTypes.Pokemon):
    def play(self):
        assert "play: " + self.name()

    def name(self):
        return "Primal Kyogre EX"

    def isWaterType(self):
        return True

