import random


class MazeGenerator:

    def __init__(self, width, height):

        self.width = width
        self.height = height
        self.path = []
        self.start_point = []
        self.dead_ends = []

    def boundary_check(self, point):
        if point[0] > self.width - 16 or point[0] < 0 or point[1] > self.height - 16 or point[1] < 0:
            return True
        else:
            return False

    def __generate_starting_point(self):
        right_bound = int((self.width - 32)/16)
        x = random.randint(1, right_bound)
        while x % 2 == 0:
            x = random.randint(1, right_bound)

        top_bound = int((self.height - 32) / 16)
        y = random.randint(1, top_bound)
        while y % 2 == 0:
            y = random.randint(1, top_bound)

        self.start_point = [x*16, y*16]

    def __generate_path(self, current_point, pathway):
        while True:
            if pathway.count([current_point[0] + 32, current_point[1]]) == 1 or self.boundary_check([current_point[0] + 32, current_point[1]]):
                if pathway.count([current_point[0] - 32, current_point[1]]) == 1 or self.boundary_check([current_point[0] - 32, current_point[1]]):
                    if pathway.count([current_point[0], current_point[1] + 32]) == 1 or self.boundary_check([current_point[0], current_point[1] + 32]):
                        if pathway.count([current_point[0], current_point[1] - 32]) == 1 or self.boundary_check([current_point[0], current_point[1] - 32]):
                            self.dead_ends.append(current_point)
                            return pathway

            x = random.randint(1, 4)

            test_point = [current_point[0], current_point[1]]
            if x == 1:
                test_point[0] += 32
                if pathway.count(test_point) == 1 or self.boundary_check(test_point):
                    continue
                else:
                    current_point = test_point
                    pathway.append(test_point)
                    pathway.append([test_point[0] - 16, test_point[1]])

            elif x == 2:
                test_point[0] -= 32
                if pathway.count(test_point) == 1 or self.boundary_check(test_point):
                    continue
                else:
                    current_point = test_point
                    pathway.append(test_point)
                    pathway.append([test_point[0] + 16, test_point[1]])

            elif x == 3:
                test_point[1] += 32
                if pathway.count(test_point) == 1 or self.boundary_check(test_point):
                    continue
                else:
                    current_point = test_point
                    pathway.append(test_point)
                    pathway.append([test_point[0], test_point[1] - 16])

            elif x == 4:
                test_point[1] -= 32
                if pathway.count(test_point) == 1 or self.boundary_check(test_point):
                    continue
                else:
                    current_point = test_point
                    pathway.append(test_point)
                    pathway.append([test_point[0], test_point[1] + 16])

            pathway = self.__generate_path(current_point, pathway)

    def redefine_goal(self):
        p = random.randint(1, len(self.dead_ends) - 1)
        return self.dead_ends[p]

    def generate_maze(self):
        """Returns the coordinates of points for the normal tiles, the starting point, and the goal"""
        self.__generate_starting_point()
        pathway = [self.start_point]
        self.path = self.__generate_path(self.start_point, pathway)

        return self.path, self.start_point