#!/usr/bin/env python
import unittest

from classes.Rover import Rover


class TestRover(unittest.TestCase):

    def test_Turn_Left(self):
        r = Rover(0, 0, "N")
        r.turnLeft()
        self.assertEqual("W", r.d)
        r.turnLeft()
        self.assertEqual("S", r.d)
        r.turnLeft()
        self.assertEqual("E", r.d)
        r.turnLeft()
        self.assertEqual("N", r.d)

    def test_Turn_Right(self):
        r = Rover(0, 0, "N")
        r.turnRight()
        self.assertEqual("E", r.d)
        r.turnRight()
        self.assertEqual("S", r.d)
        r.turnRight()
        self.assertEqual("W", r.d)
        r.turnRight()
        self.assertEqual("N", r.d)

    def test_Move_Forward(self):
        r = Rover(0, 0, "N")
        r.move()
        self.assertEqual(1, r.y)
        r.turnRight()
        r.move()
        self.assertEqual(1, r.x)
        r.turnRight()
        r.move()
        self.assertEqual(0, r.y)
        r.turnRight()
        r.move()
        self.assertEqual(0, r.x)
        r.move()
        self.assertEqual(-1, r.x)




if __name__ == '__main__':
    unittest.main()