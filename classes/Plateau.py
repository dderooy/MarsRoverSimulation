#!/usr/bin/env python
from classes.Rover import Rover

"""
Plateau represents the plane or surface the rovers land on. Contains functions to check for boundary and 
collision errors. The final answers are stored in 'finalPositions'
"""
class Plateau:

    def __init__(self, boundary, roverPlans):
        self.boundary = boundary
        self.roverPlans = roverPlans
        self.finalPositions = []

    # checks for boundary errors
    def inBoundary(self, x, y):
        if 0 <= x <= self.boundary[0] and 0 <= y <= self.boundary[1]:
            return True
        else:
            raise ValueError("Error: {}\n. Rover has gone out of bounds!")
            return False

    # checks for collisions with previous rovers
    def noCollision(self, x, y):
        for p in self.finalPositions:
            if x == p[0] and y == p[1]:
                raise ValueError("Error: {}\n. Rover has crashed into a previous rover!")
                return False
            else:
                continue
        return True

    # plots all the rover plans and checks collisions and boundaries. Stores final resutls in 'finalPositions'
    def plotRoverCourses(self):
        for plan in self.roverPlans:
            rover = Rover(plan.start_x, plan.start_y, plan.start_d)
            for command in plan.commands:
                self.maneuver(command, rover)
                if self.inBoundary(rover.x, rover.y) and self.noCollision(rover.x, rover.y):
                    continue
            self.add_finalPosition([rover.x, rover.y, rover.d])

    # convenience method for readability
    @staticmethod
    def maneuver(command, rover):
        if command == "L":
            rover.turnLeft()
        elif command == "R":
            rover.turnRight()
        elif command == "M":
            rover.move()

    # list of final results
    @property
    def finalPositions(self):
        return self.__finalPositions

    def add_finalPosition(self, p):
        self.finalPositions.append(p)


