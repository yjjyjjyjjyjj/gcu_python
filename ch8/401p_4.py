class Rectangle:
    def __init__(self,x,y,w,h):
        self.__x=x
        self.__y=y
        self.__w=w
        self.__h=h

    def getX(self):
        return self.__x

    def setX(self,x):
        self.__x = x

    def getY(self):
        return self.__y

    def setY(self,y):
        self.__y = y

    def getW(self):
        return self.__w

    def setW(self, w):
        self.__w = w

    def getH(self):
        return self.h

    def setH(self,h):
        self.__h = h

    def getArea(self):
        return self.__w * self.__h

    def overlap(self, r):
        if self.__x == r.getX()

    def __str__(self):
        return 'x좌표 : %g,  y좌표 : %g, 너비 : %g,  높이 : %g' % (self.__x, self.__y, self.__w,self.__h)

r1 = Rectangle(0,0,100,100)
print(r1)

