""" Contains al dictionaries and list from National Bridge Inventory Records"""

__author__ = "Akshay Kale"
__copyright__ = "GPL"
__credit__ = []
__email__ = 'akale@unomaha.edu'

# key: State code
# Value: Abbreviation of the state
code_state_mapping = { '25':'MA',
                       '04':'AZ',
                       '08':'CO',
                       '38':'ND',
                       '09':'CT',
                       '19':'IA',
                       '26':'MI',
                       '48':'TX',
                       '35':'NM',
                       '17':'IL',
                       '51':'VA',
                       '23':'ME',
                       '16':'ID',
                       '36':'NY',
                       '56':'WY',
                       '29':'MO',
                       '39':'OH',
                       '28':'MS',
                       '11':'DC',
                       '21':'KY',
                       '18':'IN',
                       '06':'CA',
                       '47':'TN',
                       '12':'FL',
                       '24':'MD',
                       '34':'NJ',
                       '46':'SD',
                       '13':'GA',
                       '55':'WI',
                       '30':'MT',
                       '54':'WV',
                       '15':'HI',
                       '32':'NV',
                       '37':'NC',
                       '10':'DE',
                       '33':'NH',
                       '44':'RI',
                       '50':'VT',
                       '42':'PA',
                       '05':'AR',
                       '20':'KS',
                       '45':'SC',
                       '22':'LA',
                       '40':'OK',
                       '72':'PR',
                       '41':'OR',
                       '27':'MN',
                       '53':'WA',
                       '01':'AL',
                       '31':'NE',
                       '02':'AK',
                       '49':'UT'
                   }

# Global Dictionary
# key: Material code according to the NBI
# Value: Name of the type of material
kind_of_material = { 1:'Concrete',
                     2:'Concrete Continuous',
                     3:'Steel',
                     4:'Steel Continuous',
                     5:'Prestressed Concrete',
                     6:'Prestressed Concrete Continuous',
                     7:'Wood or Timber',
                     8:'Masonry',
                     9:'Aluminum, Wrought Iron, or Cast Iron',
                     10:'Other'
                   }

# Global Dictionary
# key: Deck protection code according to the NBI
# Value: Name of the type of deck protection
deck_protection = {
                    '1':'Epoxy Coated Reinforcing',
                    '2':'Galvanized Reinforcing',
                    '3':'Other Coated Reinforcing',
                    '4':'Cathodic Protection',
                    '6':'Polymer Impregnated',
                    '7':'Internally Sealed',
                    '8':'Unknown',
                    '9':'Other',
                    '0':'None',
                    'N':'Not Applicable'
                  }

# Global Dictionary
# key: Structure type code according to the NBI
# Value: Name of the type of structure
structure_type = {
                    1:'Slab',
                    2:'Stringer/Multi-beam or Girder',
                    3:'Girder and Floorbeam System',
                    4:'Tee Beam',
                    5:'Box Beam or Girders - Multiple',
                    6:'Box Beam or Girders - Single or Spread',
                    7:'Frame (except frame culverts)',
                    8:'Orthotropic',
                    9:'Truss - Deck',
                    10:'Truss - Thru',
                    11:'Arch - Deck',
                    12:'Arch - Thru',
                    13:'Suspension',
                    14:'Stayed Girder',
                    15:'Movable - Lift',
                    16:'Movable - Bascule',
                    17:'Movable - Swing',
                    18:'Tunnel',
                    19:'Culvert (includes f1rame culverts)',
                    20:'Mixed types',
                    21:'Segmental Box Girder',
                    22:'Channel Beam',
                    0:'Other'
                 }

# Global Dictionary
# key: Owner type code according to the NBI
# Value: Name of the type of the owner type
owner_essential = {
                    1: 'State or Highway Agency',
                    2: 'County Highway Agency',
                    3: 'Town or Township Highway Agency',
                    4: 'City or Manicipal Highway Agency'
                  }

# Global Dictionary
# key: Owner type code according to the NBI
# Value: Name of the type of the owner type
owner = {
            1:  'State or Highway Agency',
            2:  'County Highway Agency',
            3:  'Town or Township Highway Agency',
            4:  'City or Manicipal Highway Agency',
            11: 'State Park, Forest, or Reservation Agency',
            12: 'Local Park, Forest, or Reservation Agency',
            21: 'Other State Agencies',
            25: 'Other Local Agencies',
            26: 'Private (other than railroad)',
            27: 'Railroad',
            31: 'State Toll Authority',
            32: 'Local Toll Authority',
            60: 'Other Federal Agencies',
            61: 'Indian Tribal Government',
            62: 'Bureau of Indian Affairs',
            63: 'Bureau of Fish and Wildlife',
            64: 'U.S. Forest Service',
            66: 'National Park Service',
            67: 'Tennessee Valley Authority',
            68: 'Bureau of Land Management',
            69: 'Bureau of Reclamation',
            70: 'Corps of Engineers (Civil)',
            71: 'Corps of Engineers (Military)',
            72: 'Air Force',
            73: 'Navy/Marine',
            74: 'Army',
            75: 'NASA',
            76: 'Metropolitan Washington Airports Service',
            80: 'Unknown',
            }
# Global Dictionary
# key: Design type code according to the NBI
# Value: Name of the type of the design code
design_load = {
               -1: 'NA',
                0: 'Other',
                1: 'H 10',
                2: 'H 15',
                3: 'HS 15',
                4: 'H 20',
                5: 'HS 20',
                6: 'HS 20 + Mod',
                7: 'Pedestrian',
                8: 'Railroad',
                9: 'HS 25'
             }
# Global Dictionary
# key: Type of wearing surface
# Value: Name of the type of wearing surface
type_of_wearing_surface = {
                "1": "Monolithic Concrete (concurrently placed with structural deck)",
                "2": "Integral Concrete (separate non-modified layer of concrete added to structural deck)",
                "3": "Latex Concrete or similar additive",
                "4": "Low Slump Concrete",
                "5": "Epoxy Overlay",
                "6": "Bituminous",
                "7": "Wood or Timber",
                "8": "Gravel",
                "9": "Other",
                "0": "None (no additional concrete thickness or wearing surface is included in the bridge deck)",
                "N":"Not Applicable (applies only to structures with no deck",
                "NA": "NA",
               }

# Global Dictionary
# key: Transition table
# Value: Transition type / Intervention type
from_to_matrix = {
                   ('8', '9'):'Repair',
                   ('7', '9'):'Repair',
                   ('6', '9'):'Repair / Reconstruction',
                   ('5', '9'):'Repair / Reconstruction',
                   ('4', '9'):'Repair / Reconstruction',
                   ('3', '9'):'Repair / Reconstruction',
                   ('2', '9'):'Repair / Reconstruction',
                   ('1', '9'):'Repair / Reconstruction',

                   ('7', '8'):'Repair',
                   ('6', '8'):'Rehabilitation',
                   ('5', '8'):'Repair / Reconstruction',
                   ('4', '8'):'Repair / Reconstruction',
                   ('3', '8'):'Repair / Reconstruction',
                   ('2', '8'):'Repair / Reconstruction',
                   ('1', '8'):'Repair / Reconstruction',

                   ('6', '7'):'Repair',
                   ('5', '7'):'Rehabilitation',
                   ('4', '7'):'Rehabilitation',
                   ('3', '7'):'Rehabilitation',
                   ('2', '7'):'Rehabilitation',
                   ('1', '7'):'Rehabilitation',

                   ('5', '6'):'Repair',
                   ('4', '6'):'Rehabilitation',
                   ('3', '6'):'Rehabilitation',
                   ('2', '6'):'Rehabilitation',
                   ('1', '6'):'Rehabilitation',

                   ('4', '5'):'Repair',
                   ('3', '5'):'Rehabilitation',
                   ('2', '5'):'Rehabilitation',
                   ('1', '5'):'Rehabilitation',

                   ('3', '4'):'Repair',
                   ('2', '4'):'Repair',
                   ('1', '4'):'Repair',
                   ('2', '3'):'Repair',
                   ('1', '2'):'Repair'

                  }


