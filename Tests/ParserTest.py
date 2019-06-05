import unittest

from Parser import Parser


class TestParser(unittest.TestCase):

    def test_Parse_Boundary(self):
        parser = Parser()
        parser.parseLine(" 5 5 ")
        self.assertEqual([5, 5], parser.boundary)

    def test_Parse_StartPoint(self):
        parser = Parser()
        parser.parseLine(" 1  2  E   ")
        self.assertEqual([1, 2, "E"], parser.allStartPoints[0])
        parser.parseLine(" 3  4W    ")
        self.assertEqual([3, 4, "W"], parser.allStartPoints[1])

    def test_Parse_Commands(self):
        parser = Parser()
        parser.parseLine("  LMlmLMlm")
        self.assertEqual("LMLMLMLM", parser.allCommands[0])
        parser.parseLine(" RM rm RM r m    ")
        self.assertEqual("RMRMRMRM", parser.allCommands[1])

    def test_Parse_RoverPlans(self):
        parser = Parser()
        parser.parseLine(" 5 5 ")
        parser.parseLine(" 1  2  E   ")
        parser.parseLine("  LMlmLMlm")
        parser.parseLine(" 3  4W    ")
        parser.parseLine(" RM rm RM r m    ")
        plans = parser.compileRoverPlans()
        self.assertEqual(2, len(plans))
        self.assertEqual([1, 2, "E"], plans[0].startPoint)
        self.assertEqual("LMLMLMLM", plans[0].commands)
        self.assertEqual([3, 4, "W"], plans[1].startPoint)
        self.assertEqual("RMRMRMRM", plans[1].commands)


if __name__ == '__main__':
    unittest.main()