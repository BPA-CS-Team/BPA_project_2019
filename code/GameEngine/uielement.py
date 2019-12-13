class UIElement:

    def __init__(self, name):
        self.image = None
        self.rect = None
        self.visible = True
        self.ui_element_manager = None
        self.name = name

    def update(self):
        pass

    def clicked_on(self, button):
        pass
