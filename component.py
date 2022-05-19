class Component:

    def __init__(self, leftDown, rightUp):
        self.validateCoordinates(leftDown, rightUp)
        self.leftDown = leftDown
        self.rightUp = rightUp

    def validateCoordinates(self, leftDown, rightUp):
        if leftDown.x > rightUp.x or leftDown.y > rightUp.y:
            raise Exception("Coordinates are not set correctly")

        
