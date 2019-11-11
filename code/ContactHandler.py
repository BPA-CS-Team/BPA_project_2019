import Box2D, GameObject

class ContactHandler(Box2D.b2ContactListener):

    def __init__(self):
        Box2D.b2ContactListener.__init__(self)

    def BeginContact(self, contact):
        contact.fixtureA.body.userData.collisionBegin(contact.fixtureB.body.userData)
        contact.fixtureB.body.userData.collisionBegin(contact.fixtureA.body.userData)

    def EndContact(self, contact):
        contact.fixtureA.body.userData.collisionEnd(contact.fixtureB.body.userData)
        contact.fixtureB.body.userData.collisionEnd(contact.fixtureA.body.userData)

    def PreSolve(self, contact, oldManifold):
        pass
    def PostSolve(self, contact, impulse):
        pass