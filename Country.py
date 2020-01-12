
class Country:

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __repr__(self):
        return "{},{}".format(self.name, self.population)
