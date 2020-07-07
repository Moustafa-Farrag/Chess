class player:

    def __init__(self, name, color):
        self.Allpieces = set()
        self.name = name
        self.color = color
        self.time = 0
        return

    def remove_piece(self, pieces):
        self.Allpieces.discard(pieces)
        return

    def add_piece(self, pieces):
        self.Allpieces.add(pieces)
        return
