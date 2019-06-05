import sys
from Plateau import Plateau
from Parser import Parser

def main ():
    parser = Parser()

    for line in sys.stdin:
        parser.parseLine(line)

    boundary = parser.boundary
    roverPlans = parser.compileRoverPlans()

    plateau = Plateau(boundary, roverPlans)
    plateau.plotRoverCourses()

    for point in plateau.finalPositions:
        sys.stdout.write("{x} {y} {d}".format(point[0], point[1], point[2]))


if __name__ == "__main__":
    main()