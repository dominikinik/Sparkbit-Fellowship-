import unittest
from  RCR import RoboticCodeRepresentationGenerator 
class TestRoboticCodeRepresentationGenerator(unittest.TestCase):
    def test_get_rcr_1(self):
        self.issued_commands = ['LEFT', 'GRAB', 'LEFT', 'BACK', 'LEFT', 'BACK', 'LEFT']

        self.generator = RoboticCodeRepresentationGenerator(self.issued_commands)

        self.assertEqual(self.generator.get_rcr("GRAB"), "00")
        self.assertEqual(self.generator.get_rcr("BACK"), "01")
        self.assertEqual(self.generator.get_rcr("LEFT"), "1")

    def test_get_rcr_2(self):
        self.issued_commands =['LEFT', 'DOWN', 'GRAB', 'LEFT', 'UP', 'UP', 'DOWN', 'DOWN', 'GRAB', 'UP', 'RIGHT', 'DROP', 'RIGHT', 'DROP', 'RIGHT', 'DROP']

        self.generator = RoboticCodeRepresentationGenerator(self.issued_commands)

        self.assertEqual(self.generator.get_rcr("DOWN"), "111")
        self.assertEqual(self.generator.get_rcr("UP"), "110")
        self.assertEqual(self.generator.get_rcr("RIGHT"), "01")
        self.assertEqual(self.generator.get_rcr("DROP"), "00")
        self.assertEqual(self.generator.get_rcr("LEFT"), "101")
        self.assertEqual(self.generator.get_rcr("GRAB"), "100")


    def test_get_rcr_3(self):
        self.issued_commands =['LEFT', 'DOWN', 'GRAB', 'UP', 'RIGHT', 'DROP']

        self.generator = RoboticCodeRepresentationGenerator(self.issued_commands)

        self.assertEqual(self.generator.get_rcr("DOWN"), "100")
        self.assertEqual(self.generator.get_rcr("UP"), "110")
        self.assertEqual(self.generator.get_rcr("RIGHT"), "01")
        self.assertEqual(self.generator.get_rcr("DROP"), "00")
        self.assertEqual(self.generator.get_rcr("LEFT"), "101")
        self.assertEqual(self.generator.get_rcr("GRAB"), "111")
    def test_get_rcr_4(self):
        self.issued_commands =['LEFT', 'DOWN', 'GRAB', 'RIGHT', 'DROP', 'RIGHT', 'DROP']

        self.generator = RoboticCodeRepresentationGenerator(self.issued_commands)

        self.assertEqual(self.generator.get_rcr("DOWN"), "011")
        self.assertEqual(self.generator.get_rcr("RIGHT"), "11")
        self.assertEqual(self.generator.get_rcr("DROP"), "10")
        self.assertEqual(self.generator.get_rcr("LEFT"), "00")
        self.assertEqual(self.generator.get_rcr("GRAB"), "010")

    def test_get_rcr_5(self):
        self.issued_commands =['LEFT', 'DOWN', 'DOWN', 'GRAB', 'UP', 'RIGHT', 'DROP']

        self.generator = RoboticCodeRepresentationGenerator(self.issued_commands)

        self.assertEqual(self.generator.get_rcr("DOWN"), "11")
        self.assertEqual(self.generator.get_rcr("UP"), "010")
        self.assertEqual(self.generator.get_rcr("RIGHT"), "101")
        self.assertEqual(self.generator.get_rcr("DROP"), "100")
        self.assertEqual(self.generator.get_rcr("LEFT"), "00")
        self.assertEqual(self.generator.get_rcr("GRAB"), "011")

if __name__ == '__main__':
    unittest.main()
