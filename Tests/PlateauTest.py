import unittest

from Plateau import Plateau


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
        with self.assertRaises(ValueError):
            p.inBoundary(-1, 0)
        with self.assertRaises(ValueError):
            p.inBoundary(0, -1)
        with self.assertRaises(ValueError):
            p.inBoundary(6, 0)
        with self.assertRaises(ValueError):
            p.inBoundary(0, 6)

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
        p.add_finalPosition([2, 3, "N"])
        p.add_finalPosition([3, 4, "N"])
        self.assertTrue(p.noCollision(2, 0))
        self.assertTrue(p.noCollision(2, 4))

    def test_Collision(self):
        p = Plateau([], [])
        p.add_finalPosition([2, 3, "N"])
        with self.assertRaises(ValueError):
            p.noCollision(2, 3)
        p.add_finalPosition([4, 6, "E"])
        with self.assertRaises(ValueError):
            p.noCollision(4, 6)
        p.add_finalPosition([8, 12, "S"])
        with self.assertRaises(ValueError):
            p.noCollision(8, 12)



