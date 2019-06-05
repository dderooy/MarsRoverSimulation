import unittest

from Plateau import Plateau
from Rover import Rover
from RoverPlan import RoverPlan


class TestPlateau(unittest.TestCase):

    def test_InBoundary(self):
        boundary = [5, 5]
        p = Plateau(boundary, [])
        self.assertTrue(p.inBoundary(0, 0))
        self.assertTrue(p.inBoundary(5, 5))
        self.assertTrue(p.inBoundary(3, 2))

    def test_OutBoundary(self):
        boundary = [5, 5]
        p = Plateau(boundary, [])
        with self.assertRaises(ValueError) as err:
            p.inBoundary(-1, 0)
        self.assertEqual("Error: {}\n. Rover has gone out of bounds!", str(err.exception))
        with self.assertRaises(ValueError) as err:
            p.inBoundary(0, -1)
        self.assertEqual("Error: {}\n. Rover has gone out of bounds!", str(err.exception))
        with self.assertRaises(ValueError) as err:
            p.inBoundary(6, 0)
        self.assertEqual("Error: {}\n. Rover has gone out of bounds!", str(err.exception))
        with self.assertRaises(ValueError) as err:
            p.inBoundary(0, 6)
        self.assertEqual("Error: {}\n. Rover has gone out of bounds!", str(err.exception))

    def test_FinalPostions(self):
        p = Plateau([], [])
        p.add_finalPosition([2, 3, "N"])
        self.assertEqual(2, p.finalPositions[0][0])
        self.assertEqual(3, p.finalPositions[0][1])
        self.assertEqual("N", p.finalPositions[0][2])
        p.add_finalPosition([4, 2, "E"])
        self.assertEqual(4, p.finalPositions[1][0])
        self.assertEqual(2, p.finalPositions[1][1])
        self.assertEqual("E", p.finalPositions[1][2])

    def test_NoCollision(self):
        p = Plateau([], [])
        self.assertTrue(p.noCollision(1, 1))
        p.add_finalPosition([2, 3, "N"])
        p.add_finalPosition([3, 4, "N"])
        self.assertTrue(p.noCollision(2, 0))
        self.assertTrue(p.noCollision(2, 4))

    def test_Collision(self):
        p = Plateau([], [])
        p.add_finalPosition([2, 3, "N"])
        with self.assertRaises(ValueError) as err:
            p.noCollision(2, 3)
        self.assertEqual("Error: {}\n. Rover has crashed into a previous rover!", str(err.exception))
        p.add_finalPosition([4, 6, "E"])
        with self.assertRaises(ValueError) as err:
            p.noCollision(4, 6)
        self.assertEqual("Error: {}\n. Rover has crashed into a previous rover!", str(err.exception))
        p.add_finalPosition([8, 12, "S"])
        with self.assertRaises(ValueError) as err:
            p.noCollision(8, 12)
        self.assertEqual("Error: {}\n. Rover has crashed into a previous rover!", str(err.exception))

    def test_Maneuver(self):
        p = Plateau([5, 5],[])
        r = Rover(0, 0, "N")
        p.maneuver("M", r)
        self.assertEqual(1, r.y)
        self.assertEqual(0, r.x)
        self.assertEqual("N", r.d)
        p.maneuver("R", r)
        self.assertEqual("E", r.d)
        p.maneuver("M", r)
        self.assertEqual(1, r.y)
        self.assertEqual(1, r.x)
        p.maneuver("R", r)
        self.assertEqual("S", r.d)

    def test_PlotCourseSuccess(self):
        plan1 = RoverPlan([1, 2, "N"], "LMLMLMLMM")
        plan2 = RoverPlan([3, 3, "E"], "MMRMMRMRRM")
        roverPlans = [plan1, plan2]

        plat = Plateau([5, 5], roverPlans)
        plat.plotRoverCourses()
        self.assertEqual(1, plat.finalPositions[0][0])
        self.assertEqual(3, plat.finalPositions[0][1])
        self.assertEqual("N", plat.finalPositions[0][2])
        self.assertEqual(5, plat.finalPositions[1][0])
        self.assertEqual(1, plat.finalPositions[1][1])
        self.assertEqual("E", plat.finalPositions[1][2])

    def test_PlotCourse_With_Boundary_Failure(self):
        plan1 = RoverPlan([1, 2, "N"], "LMLMLMLMM")
        plan2 = RoverPlan([3, 3, "E"], "MMRMMRMRRM")
        roverPlans = [plan1, plan2]

        plat = Plateau([4, 4], roverPlans)
        with self.assertRaises(ValueError) as err:
            plat.plotRoverCourses()
        self.assertEqual("Error: {}\n. Rover has gone out of bounds!", str(err.exception))

    def test_PlotCourse_With_Collision(self):
        plan1 = RoverPlan([1, 2, "N"], "LMLMLMLMM")
        plan2 = RoverPlan([2, 1, "N"], "MMLMMRM")
        roverPlans = [plan1, plan2]

        plat = Plateau([5, 5], roverPlans)
        with self.assertRaises(ValueError) as err:
            plat.plotRoverCourses()
        self.assertEqual("Error: {}\n. Rover has crashed into a previous rover!", str(err.exception))





