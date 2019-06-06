#!/usr/bin/env python
import sys
from classes.Plateau import Plateau
from classes.Parser import Parser

"""
Main function. Parses input, processes results, and outputs answers.
"""
def main ():
    parser = Parser()

    # read input from piped data
    for line in sys.stdin:
        line = line.rstrip()
        parser.parseLine(line)

    # throw error if something is wrong with input
    if not parser.boundary or not parser.allStartPoints or not parser.allCommands:
        raise ValueError("Error: {}\n. Something went wrong with the input")
    if len(parser.allStartPoints) != len(parser.allCommands):
        raise ValueError("Error: {}\n. Missing some data!")

    # setup plateau object and pass along the surface boundary and list of roverPlans
    plateau = Plateau(parser.boundary, parser.compileRoverPlans())

    # plot the rover paths along the plateau and compile the final rover positions
    plateau.plotRoverCourses()

    # output the final results
    for point in plateau.finalPositions:
        print("{} {} {}".format(point[0], point[1], point[2]))


if __name__ == "__main__":
    main()