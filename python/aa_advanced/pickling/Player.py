class Player:

    def __init__(self, ID, name, health, items):
        self.id = ID
        self.name = name
        self.health = health
        self.items = items

    def __str__(self):
        return "My ID: " + str(self.id) + \
            " \nMy Name: " + self.name + \
            " \nMy Health: " + str(self.health) + \
            " \nMy Items: " + str(self.items) + "."
