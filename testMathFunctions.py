#import statements
import unittest
import mathFunctions

class Knownvalues(unittest.TestCase):
#test areaCircle() pi r ^2
    def test_areaCircle_for_10radius(self):    
        #get the results of the function
        result = mathFunctions.areaCircle(10)
        #check for the expected ouput
        expected= 314.1592653589793
        self.assertEqual(expected, result)

class Knowvlues(unittest.TestCase):
     #test areaCircle() pi r ^2
    def test_areaCircle_for_2radius(self):    
        #get the results of the function
        result = mathFunctions.areaCircle(2)
        #check for the expected ouput
        expected= 12.566370614359172
        self.assertEqual(expected, result)


class Knownvlues(unittest.TestCase):
    #test areaCircle() pi r ^2
    def test_areaCircle_for_6radius(self):    
        #get the results of the function
        result = mathFunctions.areaCircle(6)
        #check for the expected ouput
        expected=113.09733552923255
        self.assertEqual(expected, result)


#run test
if __name__ == '__main__':
    unittest.main()