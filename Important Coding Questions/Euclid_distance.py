class Point:

    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y

    def __str__(self):
        return '<{},{}>'.format(self.x_coord, self.y_coord)

    def euclidean_distance(self, other):
        return ((self.x_coord - other.x_coord) ** 2 + (self.y_coord - other.y_coord) ** 2) ** 0.5

    def distance_from_origin(self):
        return self.euclidean_distance(Point(3,7))


p1 = Point(0, 0)
p2 = Point(3, 6)
distance = p1.distance_from_origin()
print("The Euclidean distance between {} and {} is: {:.2f}".format(p1, p2, distance))
