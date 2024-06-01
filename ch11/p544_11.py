class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def __add__(self, other_circle):
        return Circle(self.__radius + other_circle.__radius)

    def __gt__(self, other_circle):
        return self.__radius > other_circle.__radius

    def __lt__(self, other_circle):
        return self.__radius < other_circle.__radius