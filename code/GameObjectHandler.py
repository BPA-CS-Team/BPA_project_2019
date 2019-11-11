import pygame, Box2D, ContactHandler


class GameObjectHandler:

    def __init__(self, gameobjects=[], b2_scale=32): #initializes box2d's (physics library) world environment
        self.world = Box2D.b2World() #create instance of box 2d world
        self.b2_scale = b2_scale # scaling reference. is equal to pixels to meter
        self.gameobjects = [] #game objects list
        self.contactHandler = ContactHandler.ContactHandler()
        self.world.contactListener = self.contactHandler

        if gameobjects: #checks to see if there are objects in list
            for gameobject in gameobjects: #iterates through list
                self.add(gameobject) #if so calls add function      

    def set_b2_scale(self, scale):
        self.b2_scale = scale

    def update(self):
        self.world.Step(1 / 60, 6, 2)

        for gameobject in self.gameobjects:
            if gameobject.physics:
                gameobject.rect.x = gameobject.body.position.x * self.b2_scale - gameobject.rect.width / 2
                gameobject.rect.y = -gameobject.body.position.y * self.b2_scale - gameobject.rect.height / 2
            gameobject.update()

    def get_images(self):
        images = []
        for gameobject in self.gameobjects:
            images.append(gameobject.image)
        return images

    def get_rects(self):
        rects = []
        for gameobject in self.gameobjects:
            rects.append(gameobject.rect)
        return rects

    def add(self, gameobject):
        self.gameobjects.append(gameobject) # adds game object to list of game objects

        if gameobject.physics: # checks if game objects have physics attributes
            body = self.world.CreateBody( # if so then, the code will create rigid body for game objects
                position=(gameobject.rect.x / self.b2_scale, -gameobject.rect.y / self.b2_scale),
                type=Box2D.b2_dynamicBody if gameobject.dynamic else Box2D.b2_staticBody,
                userData=gameobject, # create references for each other 
                fixedRotation=True)
            body.CreatePolygonFixture(box=(gameobject.rect.width / 2 / self.b2_scale, gameobject.rect.height / 2 / self.b2_scale), density=1, friction=0.5)
            gameobject.body = body


