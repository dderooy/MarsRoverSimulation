#!/usr/bin/env python
import sys
from classes.Plateau import Plateau
from classes.Parser import Parser

"""
Main function. Parses input, processes results, and outputs answers.
"""
def main ():
    parser = Parser()

    for line in sys.stdin:
        line = line.rstrip()
        parser.parseLine(line)

    boundary = parser.boundary
    roverPlans = parser.compileRoverPlans()

    plateau = Plateau(boundary, roverPlans)
    plateau.plotRoverCourses()

    for point in plateau.finalPositions:
        print("{} {} {}".format(point[0], point[1], point[2]))


if __name__ == "__main__":
    main()