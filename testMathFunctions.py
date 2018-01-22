#import statements
import unittest
import MathFunctions

class Knownvalues(unittest.TestCase)
#test areaCircle() pi r ^2
    def test_areaCircle_for_10radius(self):    
        #get the results of the function
        result = MathFunctions.areaCircle(10)
        #check for the expected ouput
        expected= 314.1592653589793
        self.assertEqual(expected, result)

if __name__ == '__main__':
    app.run()