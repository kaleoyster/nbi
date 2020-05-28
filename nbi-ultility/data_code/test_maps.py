""" Contains test functions of maps"""
import unittest
import maps

__author__ = "Akshay Kale"
__copyright__ = "GPL"
__credit__ = []
__email__= "akale@unomaha.edu"

class TestMaps(unittest.TestCase):
    #code_material  = maps.kind_of_material
    #code_deck_protec = maps.deck_protection
    #code_structure = maps.structure_type
    code_owner_mini = maps.owner_essential
    #code_owner = maps.owner_code
    code_design = maps.design_load


    def test_code_state_mapping(self):
        # check all states must be in the list
        code_state = maps.code_state_mapping
        #INPUT to check the number of states is 52 
        size_code_state = len(code_state)
        self.assertEqual(size_code_state, 52)
        input_code_ne = '31' # Nebraska
        input_code_ak = '02' # Alaska
        input_code_ks = '20' # Kansas

        self.assertEqual(code_state[input_code_ne], 'NE')
        self.assertEqual(code_state[input_code_ak], 'AK')
        self.assertEqual(code_state[input_code_ks], 'KS')

    def test_from_to_matrix(self):
        pass

    def design_load(self):
        code_design = maps.design_load

        #INPUT to check the number of states is  
        self.assertEqual(len(code_design), 11)

        input_code_NA = -1   # NA
        input_code_0  =  0   # Other
        input_code_5  =  5   # HS 20

        self.assertEqual(code_NA[input_code_NA], "NA")
        self.assertEqual(code_0[input_code_0], 'Other')
        self.assertEqual(code_5[input_code_5], 'HS ')


    def owner_essential(self):
        pass

    def owners(self):
        pass

    def structure_type(self):
        pass

    def deck_protection(self):
        pass

    def kind_of_material(self):
        pass

    def code_state_mapping(self):
        pass
"""
    def type_of_wearing(self):
        type_wearing = maps.type_of_wearing_surface

        self.assertEqual(len(type_wearing), 2)

        # INPUT
        self.assertEqual(type_wearing[1], "Monolithic Concrete (concurrently placed with structural deck)")
"""
if __name__ == "__main__":
   unittest.main()
