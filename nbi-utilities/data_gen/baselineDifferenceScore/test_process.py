"""Contains test function of the data function"""
import unittest
import numpy as np
import process

__author__ = 'Akshay Kale'
__copyright__ = 'GPL'
__credit__ = []
__email__ = 'akale@unomaha.edu'

class TestData(unittest.TestCase):
     def test_get_values(self):
         dc = process.DataChef()

         # INPUT
         dictionary  = {
                        1:'One',
                        2:'Two',
                        3:'Three',
                       }
         # OUTPUT
         keys = [
                 1,
                 2,
                 3,
                ]

         # OUTPUT
         output = ['One', 'Two', 'Three']
         self.assertEqual(dc.get_values(keys, dictionary), output)

     def test_create_dictionary(self):
         dc = process.DataChef()

         # INPUT
         keys = [
                 1,
                 2,
                 3,
                 ]

         # VALUES
         values = [
                   'one',
                   'two',
                   'three'
                  ]

         # OUTPUT
         output = {
                    1: 'one',
                    2: 'two',
                    3: 'three',
                    }

         self.assertEqual(dc.create_dictionary(keys, values), output)

     def test_is_same_elements(self):
         dc = process.DataChef()

         #INPUT
         elements_1 = [2, 2, 2, 2]
         elements_2 = ['same', 'same', 'same', 'same']
         elements_3 = ['one', 'two', 'three']

         self.assertTrue(dc.is_same_elements(elements_1))
         self.assertTrue(dc.is_same_elements(elements_2))
         self.assertFalse(dc.is_same_elements(elements_3))


     def test_calculate_age(self):
         dc = process.DataChef()

         #INPUT
         year_built = [2000, 2000, 2000, 2002]
         year_survey = [2020, 2002, 2001, 2010]

         #OUTPUT 
         output = [18, 2, 1, 8]

         self.assertEquals(dc.calculate_age(year_built, year_survey), np.array(output).all())

if __name__ == "__main__":
    unittest.main()
