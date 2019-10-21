class GameObject:

    def __init__(self):
        self.image = None
        self.rect = None
        self.physics = False
        self.dynamic = False
        self.body = None
        self.active = True

    def update(self):
        pass
