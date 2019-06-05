import re
from RoverPlan import RoverPlan

class Parser:

    def __init__(self):
        self.allStartPoints =[]
        self.allCommands = []
        self.boundary = []
        self.roverPlans = []

    def parseLine(self, line):
        line = line.replace(' ', '')
        patternLRM = re.compile("^[MRL]*$")

        if len(line) == 2 and line.isdigit():
            self.boundary = list(line)
            self.boundary = map(int, self.boundary)
        elif len(line) == 3 and line[0].isdigit() and line[1].isdigit() and line[2].isalpha():
            startPoint = list(line)
            startPoint[0] = int(startPoint[0])
            startPoint[1] = int(startPoint[1])
            startPoint[2] = startPoint[2].upper()
            self.allStartPoints.append(startPoint)
        elif line.isalpha() and patternLRM.match(line.upper()):
            commands = line.upper()
            self.allCommands.append(commands)

    def compileRoverPlans(self):
        self.roverPlans = []
        for point, command in zip(self.allStartPoints, self.allCommands):
            self.roverPlans.append(RoverPlan(point, command))
        return self.roverPlans

    @property
    def boundary(self):
        return self.boundary;

    @property
    def allStartPoints(self):
        return self.allStartPoints;

    @property
    def allCommands(self):
        return self.allCommands;
