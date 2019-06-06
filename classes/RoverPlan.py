#!/usr/bin/env python

"""
RoverPlan is used to store each rover start point and command string. It also helps improve code readability.
"""
class RoverPlan:

    def __init__(self, start, commands):
        self.start = start
        self.commands = commands

    @property
    def start_x(self):
        return self.start[0]

    @property
    def start_y(self):
        return self.start[1]

    @property
    def start_d(self):
        return self.start[2]

    @property
    def commands(self):
        return self.commands

    @property
    def startPoint(self):
        return [self.start_x, self.start_y, self.start_d]
