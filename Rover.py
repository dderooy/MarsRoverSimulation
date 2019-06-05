

class Rover:
    
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def d(self):
        return self.__d

    @d.setter
    def d(self, d):
        self.__d = d


    def turnLeft(self):
        if self.d == "N":
            self.d = "W"
        elif self.d == "W":
            self.d = "S"
        elif self.d == "S":
            self.d = "E"
        elif self.d == "E":
            self.d = "N"

    def turnRight(self):
        if self.d == "N":
            self.d = "E"
        elif self.d == "E":
            self.d = "S"
        elif self.d == "S":
            self.d = "W"
        elif self.d == "W":
            self.d = "N"

    def move(self):
        if self.d == "N":
            self.y += 1
        elif self.d == "E":
            self.x += 1
        elif self.d == "S":
            self.y -= 1
        elif self.d == "W":
            self.x -= 1