import sys
import re
from RoverPlan import RoverPlan
from Plateau import Plateau

def main ():
    allStartPoints =[]
    allCommands = []
    roverPlans = []

    for line in sys.stdin:
        line.strip()
        line.replace(" ", "")
        patternLRM = re.compile("^[MRL]*$")

        if len(line) == 2 and line.isdigit():
            boundary = list(line)
        elif len(line) == 3 and line[0].isdigit() and line[1].isdigit() and line[2].isalpha():
            startPoint = list(line)
            startPoint[2] = startPoint[2].upper()
            allStartPoints.append(startPoint)
        elif line.isalpha() and patternLRM.match(line):
            commands = line.upper()
            allCommands.append(commands)

    for point, command in zip(allStartPoints, allCommands):
        roverPlans.append(RoverPlan(point, command))

    plateau = Plateau(boundary, roverPlans)
    plateau.plotRoverCourses()

    for point in plateau.finalPositions:
        sys.stdout.write("{x} {y} {d}".format(point[0], point[1], point[2]))


if __name__ == "__main__":
    main()