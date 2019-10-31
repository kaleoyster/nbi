#!/Usr/bin/env python

""" Provides operations for processing National Bridge Inventory (NBI) inspection record.
    
"""
import csv
import pandas as pd
import numpy as np
import requests 
import io

__author__ = "Akshay Kale"
__copyright__ = "GPL"
__credits__ = ['Jonathan Monical']
__email__ = "akale@unomaha.edu"

class Data():
    def __init__(self):
        """ Returns a new data object 
        """
        self.url = None
        self.state = None
        self.year = None
        self.NEW_NAMES_DICT ={'STATE_CODE_001': '1: State Code',
                              'STRUCTURE_NUMBER_008': '8: Structure Number',
                              'RECORD_TYPE_005A': '5A: Record Type',
                              'ROUTE_PREFIX_005B' : '5B: Route Signing Prefix',
                              'SERVICE_LEVEL_005C': '5C: Designated Level of Service',
                              'ROUTE_NUMBER_005D': '5D: Route Number',
                              'DIRECTION_005E': '5E: Directional Suffix',
                              'HIGHWAY_DISTRICT_002': '2: Highway Agency District',
                              'COUNTY_CODE_003': '3: County (Parish) Code',
                              'PLACE_CODE_004': '4: Place Code',
                              'FEATURES_DESC_006A': '6A: Features Intersected',
                              'CRITICAL_FACILITY_006B': '6B: Critical Facility Indicator',
                              'FACILITY_CARRIED_007': '7: Facility Carried By Structure',
                              'LOCATION_009': '9: Location',
                              'MIN_VERT_CLR_010': '10: Inventory Rte, Min Vert Clearance',
                              'KILOPOINT_011': '11: Kilometerpoint',
                              'BASE_HWY_NETWORK_012': '12: Base Highway Network',
                              'LRS_INV_ROUTE_013A': '13A: LRS Inventory Route',
                              'SUBROUTE_NO_013B': '13B: Subroute Number',
                              'LAT_016': '16: Latitude',
                              'LONG_017': '17: Longitude',
                              'DETOUR_KILOS_019': '19: Bypass/Detour Length',
                              'TOLL_020': '20: Toll',
                              'MAINTENANCE_021': '21: Maintenance Responsibility',
                              'OWNER_022': '22: Owner',
                              'FUNCTIONAL_CLASS_026': '26: Functional Class Of Inventory Rte.',
                              'YEAR_BUILT_027': '27: Year Built',
                              'TRAFFIC_LANES_ON_028A': '28A: Lanes On Structure',
                              'TRAFFIC_LANES_UND_028B': '28B: Lanes Under Structure',
                              'ADT_029': '29: Average Daily Traffic',
                              'YEAR_ADT_030': '30: Year Of Average Daily Traffic',
                              'DESIGN_LOAD_031': '31: Design Load',
                              'APPR_WIDTH_MT_032': '32: Approach Roadway Width',
                              'MEDIAN_CODE_033': '33: Bridge Median',
                              'DEGREES_SKEW_034': '34: Skew',
                              'STRUCTURE_FLARED_035': '35: Structure Flared',
                              'RAILINGS_036A': '36A: Bridge Railings',
                              'TRANSITIONS_036B': '36B: Transitions',
                              'APPR_RAIL_036C': '36C: Approach Guardrail',
                              'APPR_RAIL_END_036D': '36D: Approach Guardrail Ends',
                              'HISTORY_037':'37: Historical significance',
                              'NAVIGATION_038':'38: Navigation Control',
                              'NAV_VERT_CLR_MT_039': '39: Navigation Vertical Clearance',
                              'NAV_HORR_CLR_MT_040': '40: Navigation Horizontal Clearance',
                              'OPEN_CLOSED_POSTED_041': '41: Structure Open/Posted/Closed',
                              'SERVICE_ON_042A': '42A: Type of Service On Bridge',
                              'SERVICE_UND_042B': '42B: Type of Service Under Bridge',
                              'STRUCTURE_KIND_043A': '43A: Kind of Material/Design',
                              'STRUCTURE_TYPE_043B': '43B: Type of Design/Construction',
                              'APPR_KIND_044A': '44A: Kind of Material/Design',
                              'APPR_TYPE_044B': '44B: Type of Design/Construction',
                              'MAIN_UNIT_SPANS_045': '45: Number Of Spans In Main Unit',
                              'APPR_SPANS_046': '46: Number Of Approach Spans',
                              'HORR_CLR_MT_047': '47: Inventory Rte Total Horz Clearance',
                              'MAX_SPAN_LEN_MT_048': '48: Length of Maximum Span',
                              'STRUCTURE_LEN_MT_049': '49: Structure Length',
                              'LEFT_CURB_MT_050A': '50A: Left Curb/Sidewalk Width',
                              'RIGHT_CURB_MT_050B': '50B: Right Curb/Sidewalk Width',
                              'ROADWAY_WIDTH_MT_051': '51: Bridge Roadway Width, Curb-To-Curb',
                              'DECK_WIDTH_MT_052': '52: Deck Width, Out-To-Out',
                              'VERT_CLR_OVER_MT_053': '53: Min Vert Clear Over Bridge Roadway',
                              'VERT_CLR_UND_REF_054A': '54A: Reference Feature',
                              'VERT_CLR_UND_054B': '54B: Minimum Vertical Underclearance',
                              'LAT_UND_REF_055A': '55A: Reference Feature',
                              'LAT_UND_MT_055B': '55B: Minimum Lateral Underclearance on Right',
                              'LEFT_LAT_UND_MT_056': '56: Min Lateral Underclear On Left',
                              'DECK_COND_058': '58: Deck',
                              'SUPERSTRUCTURE_COND_059': '59: Superstructure',
                              'SUBSTRUCTURE_COND_060': '60: Substructure',
                              'CHANNEL_COND_061': '61: Channel/Channel Protection',
                              'CULVERT_COND_062': '62: Culverts',
                              'OPR_RATING_METH_063': '63: Method Used To Determine Operating Rating',
                              'OPERATING_RATING_064': '64: Operating Rating',
                              'INV_RATING_METH_065': '65: Method Used To Determine Inventory Rating',
                              'INVENTORY_RATING_066': '66: Inventory Rating',
                              'STRUCTURAL_EVAL_067': '67: Structural Evaluation',
                              'DECK_GEOMETRY_EVAL_068': '68: Deck Geometry',
                              'UNDCLRENCE_EVAL_069': '69: Underclear, Vertical & Horizontal',
                              'POSTING_EVAL_070': '70: Bridge Posting',
                              'WATERWAY_EVAL_071': '71: Waterway Adequacy',
                              'APPR_ROAD_EVAL_072': '72: Approach Roadway Alignment',
                              'WORK_PROPOSED_075A': '75A: Type of Work Proposed',
                              'WORK_DONE_BY_075B': '75B: Work Done By',
                              'IMP_LEN_MT_076': '76: Length of Structure Improvement',
                              'DATE_OF_INSPECT_090': '90: Inspection Date',
                              'INSPECT_FREQ_MONTHS_091': '91: Designated Inspection Frequency',
                              'FRACTURE_092A': '92A: Fracture Critical Details',
                              'UNDWATER_LOOK_SEE_092B': '92B: Underwater Inspection',
                              'SPEC_INSPECT_092C': '92C: Other Special Inspection',
                              'FRACTURE_LAST_DATE_093A': '93A: Fracture Critical Details Date',
                              'UNDWATER_LAST_DATE_093B': '93B: Underwater Inspection Date',
                              'SPEC_LAST_DATE_093C': '93C: Other Special Inspection Date',
                              'BRIDGE_IMP_COST_094': '94: Bridge Improvement Cost',
                              'ROADWAY_IMP_COST_095': '95: Roadway Improvement Cost',
                              'TOTAL_IMP_COST_096': '96: Total Project Cost',
                              'YEAR_OF_IMP_097': '97: Year Of Improvement Cost Estimate',
                              'OTHER_STATE_CODE_098A': '98A: Neighboring State Code',
                              'OTHER_STATE_PCNT_098B': '98B: Percent Responsibility',
                              'OTHR_STATE_STRUC_NO_099': '99: Border Bridge Structure Number',
                              'STRAHNET_HIGHWAY_100': '100: STRAHNET Highway Designation',
                              'PARALLEL_STRUCTURE_101': '101: Parallel Structure Designation',
                              'TRAFFIC_DIRECTION_102': '102: Direction Of Traffic',
                              'TEMP_STRUCTURE_103': '103: Temporary Structure Designation',
                              'HIGHWAY_SYSTEM_104': '104: Highway System Of Inventory Route',
                              'FEDERAL_LANDS_105': '105: Federal Lands Highways',
                              'YEAR_RECONSTRUCTED_106': '106: Year Reconstructed',
                              'DECK_STRUCTURE_TYPE_107': '107: Deck Structure Type',
                              'SURFACE_TYPE_108A': '108A: Type of Wearing Surface',
                              'MEMBRANE_TYPE_108B': '108B: Type of Membrane',
                              'DECK_PROTECTION_108C': '108C: Deck Protection',
                              'PERCENT_ADT_TRUCK_109': '109: AVERAGE DAILY TRUCK TRAFFIC',
                              'NATIONAL_NETWORK_110': '110: DESIGNATED NATIONAL NETWORK',
                              'PIER_PROTECTION_111': '111: PIER/ABUTMENT PROTECTION',
                              'BRIDGE_LEN_IND_112': '112: NBIS BRIDGE LENGTH',
                              'SCOUR_CRITICAL_113': '113: SCOUR CRITICAL BRIDGES',
                              'FUTURE_ADT_114': '114: FUTURE AVERAGE DAILY TRAFFIC',
                              'YEAR_OF_FUTURE_ADT_115': '115: YEAR OF FUTURE AVG DAILY TRAFFIC',
                              'MIN_NAV_CLR_MT_116': '116: MINIMUM NAVIGATION VERTICAL CLEARANCE VERTICAL LIFT BRIDGE',
                              'SUFFICIENCY_RATING' :'SR',
                              'FED_AGENCY': 'Federal Agency'
                             }

        self.COL_IGNORED = [ 'DATE_LAST_UPDATE',
                             'TYPE_LAST_UPDATE',
                             'DEDUCT_CODE',
                             'REMARKS',
                             'PROGRAM_CODE',
                             'PROJ_NO',
                             'PROJ_SUFFIX',
                             'NBI_TYPE_OF_IMP',
                             'DTL_TYPE_OF_IMP',
                             'SPECIAL_CODE',
                             'STEP_CODE',
                             'STATUS_WITH_10YR_RULE',
                             'SUFFICIENCY_ASTERC',
                             'STATUS_NO_10YR_RULE',
                             'CAT10',
                             'CAT23',
                             'CAT29'
                             ]

        self.RENAMECOLS = { '1: State Code':'State',
                            '16: Latitude':'Latitude',
                            '17: Longitude':'Longitude',
                            '27: Year Built':'Built in',
                            '58: Deck':'Deck',
                            '59: Superstructure':'Super',
                            '60: Substructure':'Sub',
                            '62: Culverts':'Culvert',
                            '28A: Lanes On Structure':'Lanes',
                            '29: Average Daily Traffic':'ADT',
                            '109: AVERAGE DAILY TRUCK TRAFFIC':'ADTT (% ADT)',
                            '31: Design Load':'Design Load',
                            '45: Number Of Spans In Main Unit':'# Spans',
                            '48: Length of Maximum Span':'Span Max Len',
                            '49: Structure Length':'Struct Length',
                            '70: Bridge Posting':'Posting',
                            '106: Year Reconstructed':'Reconst. Year',
                            '108A: Type of Wearing Surface':'Wearing Surface',
                            '108B: Type of Membrane':'Membrane',
                            '108C: Deck Protection':'Deck Protection',
                            '55B: Minimum Lateral Underclearance on Right':'55B: Minimum Lateral Underclearance',

                             '76: Length of Structure Improvement':'76: Length Of Structure Improvement',
                             '51: Bridge Roadway Width, Curb-To-Curb':'51: Bridge Roadway Width Curb-To-Curb'
                          }

        self.DATACENTER_CODES = {31:317}


    def getData(self, url):
        """Returns a pandas dataframe by downloading the csvfile from url
            
            url: A valid url to a csvfile
        """
        self.url = url
        requested_csv = requests.get(url).content
        return pd.read_csv(io.StringIO(requested_csv.decode('utf-8')), low_memory = False)

    def renameDataColumns(self, df):
        """Renames the columns of the dataframe and returns the new dataframe
           
           df: A pandas dataframe who's Column names to be renamed

           NOTE: df's column name will be changed according to the global variable NEW_NAMES_DICT
        """
        # get DF and names dict and return new named DF
        df = df.rename(columns=self.NEW_NAMES_DICT)
        return df

    def dropIgnoredColumns(self, df):
        """drops columns of the dataframe specified by global variable COL_IGNORED and returns the dataframe
           
           NOTE: df's column name will be changed according to the global variable COL_IGNORED
        """
        df = df.drop(self.COL_IGNORED, axis = 1)
        return df

    def renameStateCodes(self, df):
        """Return pandas dataframe with renamed column '1: State Code' according to the global variable DATACENTER_CODES
          
          df: A pandas dataframe
          
          NOTE: df's column '1: State Code' will be changed according to the global variabe DATACENTER_CODES
        """
        df['1: State Code'] = df['1: State Code'].map(self.DATACENTER_CODES)
        return df

    def convertGeocoordinate(self, geocoordinate):
        """Returns pandas dataframe with converted geo-coordinates
           
           geocoordinate: A valid longitude or longitude in the format: " "
        """
        if len(geocoordinate) == 9 and geocoordinate[0] == '1':
            result = int(geocoordinate[:3]) \
                     + (int(geocoordinate[3:5]) / 600) \
                     + (int(geocoordinate[5:]) / 360000)
            return result

        else:
            result = int(geocoordinate[:2]) \
                    + (int(geocoordinate[2:4]) / 600) \
                    + (int(geocoordinate[4:]) / 360000)    
            return result
    
    def createCaseName(self, df):
        """Return a pandas dataframe with a new column Case Name, Case Name = 'df[column14] at df[column16] at df[column17]' """
        
        df["Case Name"] = df[['6A: Features Intersected', '7: Facility Carried By Structure', '9: Location']].apply(lambda x: ' at '.join(x), axis = 1)
        return df

    def createCaseId(self, df):
        """Return a pandas dataframe with a new column CaseId, CaseId = df['8: Structure Number']"""

        df['Case Id'] = df['8: Structure Number']
        return df

    def createYear(self, df):
        """Returns a pandas dataframe with a new column Year, Year = url-of-the-file[6th position]"""
        df['Year'] =  int(self.url.split("/")[5])
        return df

    def createMaterialColumn(self, df):
        """Returns a pandas dataframe with a new column Material, Material = kind_of_material['43A: Kind of Material/Design'] """
           
        kind_of_material = {
                            1:"Concrete",
                            2:"Concrete Continuous",
                            3:"Steel",
                            4:"Steel Continuous",
                            5:"Prestressed Concrete",
                            6:"Prestressed Concrete Continuous",
                            7:"Wood or Timber",
                            8:"Masonry",
                            9:"Aluminum, Wrought Iron, or Cast Iron",
                            0:"Other",
                       }
    
        df['Material'] = df['43A: Kind of Material/Design'].map(kind_of_material)

        return df

    def createConstructionTypeColumn(self, df):
        """Returns a pandas dataframe with a new column Construction Type, ConstructionType = type_of_construction['43B: Type of Design/Construction'] """
        
        type_of_construction = {
                                1:"Slab",
                                2:"Stringer/Multi-beam or Girder",
                                3:"Girder and Floorbeam System",
                                4:"Tee Beam",
                                5:"Box Beam or Girders - Multiple",
                                6:"Box Beam or Girders - Single ofinr Spread",
                                7:"Frame (except culverts)",
                                8:"Orthotropic",
                                9:"Truss - Deck",
                                10:"Truss - Thru",
                                11:"Arch - Deck",
                                12:"Arch - Thru",
                                13:"Suspension",
                                14:"Stayed Girder",
                                15:"Movable - Lift",
                                16:"Movable - Bascule",
                                17:"Movable - Swing",
                                18:"Tunnel",
                                19:"Culvert (includes frame culverts)",
                                20:"Mixed types",
                                21:"Segmental Box Girder",
                                22:"Channel Beam",
                                0:"Other"
                                }

        df['Construction Type'] = df['43B: Type of Design/Construction'].map(type_of_construction)
        return df

    def renameCols(self, df):
        """ Returns a pandas dataframe with new renamed columns """
        df = df.rename(columns=self.RENAMECOLS)
        return df

    def rearrangeCols(self, df):
        
        rearrange = [   'Case Name',
                'Case Id',
                'Year',
                'State',
                '8: Structure Number',
                '5A: Record Type',
                '5B: Route Signing Prefix',
                '5C: Designated Level of Service',
                '5D: Route Number',
                '5E: Directional Suffix',
                '2: Highway Agency District',
                '3: County (Parish) Code',
                '4: Place Code',
                '6A: Features Intersected',
                '6B: Critical Facility Indicator',
                '7: Facility Carried By Structure',
                '9: Location',
                '10: Inventory Rte, Min Vert Clearance',
                '11: Kilometerpoint',
                '12: Base Highway Network',
                '13A: LRS Inventory Route',
                '13B: Subroute Number',
                'Latitude',
                'Longitude',
                '19: Bypass/Detour Length',
                '20: Toll',
                '21: Maintenance Responsibility',
                '22: Owner',
                '26: Functional Class Of Inventory Rte.',
                'Built in',
                'Material',
                'Construction Type',
                'Deck',
                'Super',
                'Sub',
                'Culvert',
                'Lanes',
                '28B: Lanes Under Structure',
                'ADT',
                'ADTT (% ADT)',
                '30: Year Of Average Daily Traffic',
                'Design Load',
                '32: Approach Roadway Width',
                '33: Bridge Median',
                '34: Skew',
                '35: Structure Flared',
                '36A: Bridge Railings',
                '36B: Transitions',
                '36C: Approach Guardrail',
                '36D: Approach Guardrail Ends',
                '37: Historical significance',
                '38: Navigation Control',
                '39: Navigation Vertical Clearance',
                '40: Navigation Horizontal Clearance',
                '41: Structure Open/Posted/Closed',
                '42A: Type of Service On Bridge',
                '42B: Type of Service Under Bridge',
                '43A: Kind of Material/Design',
                '43B: Type of Design/Construction',
                '44A: Kind of Material/Design',
                '44B: Type of Design/Construction',
                '# Spans',
                '46: Number Of Approach Spans',
                '47: Inventory Rte Total Horz Clearance',
                'Span Max Len',
                'Struct Length',
                '50A: Left Curb/Sidewalk Width',
                '50B: Right Curb/Sidewalk Width',
                '51: Bridge Roadway Width Curb-To-Curb',
                '52: Deck Width, Out-To-Out',
                '53: Min Vert Clear Over Bridge Roadway',
                '54A: Reference Feature',
                '54B: Minimum Vertical Underclearance',
                '55A: Reference Feature',
                '55B: Minimum Lateral Underclearance',
                '56: Min Lateral Underclear On Left',
                '61: Channel/Channel Protection',
                '63: Method Used To Determine Operating Rating',
                '64: Operating Rating',
                '65: Method Used To Determine Inventory Rating',
                '66: Inventory Rating',
                '67: Structural Evaluation',
                '68: Deck Geometry',
                '69: Underclear, Vertical & Horizontal',
                'Posting',
                '71: Waterway Adequacy',
                '72: Approach Roadway Alignment',
                '75A: Type of Work Proposed',
                '75B: Work Done By',
                '76: Length Of Structure Improvement',
                '90: Inspection Date',
                '91: Designated Inspection Frequency',
                '92A: Fracture Critical Details',
                '92B: Underwater Inspection',
                '92C: Other Special Inspection',
                '93A: Fracture Critical Details Date',
                '93B: Underwater Inspection Date',
                '93C: Other Special Inspection Date',
                '94: Bridge Improvement Cost',
                '95: Roadway Improvement Cost',
                '96: Total Project Cost',
                '97: Year Of Improvement Cost Estimate',
                '98A: Neighboring State Code',
                '98B: Percent Responsibility',
                '99: Border Bridge Structure Number',
                '100: STRAHNET Highway Designation',
                '101: Parallel Structure Designation',
                '102: Direction Of Traffic',
                '103: Temporary Structure Designation',
                '104: Highway System Of Inventory Route',
                '105: Federal Lands Highways',
                'Reconst. Year',
                '107: Deck Structure Type',
                'Wearing Surface',
                'Membrane',
                'Deck Protection',
                '110: DESIGNATED NATIONAL NETWORK',
                '111: PIER/ABUTMENT PROTECTION',
                '112: NBIS BRIDGE LENGTH',
                '113: SCOUR CRITICAL BRIDGES',
                '114: FUTURE AVERAGE DAILY TRAFFIC',
                '115: YEAR OF FUTURE AVG DAILY TRAFFIC',
                '116: MINIMUM NAVIGATION VERTICAL CLEARANCE VERTICAL LIFT BRIDGE',
                'Federal Agency',
                'SR'
            ]
        df = df[rearrange]
        return df
        

def main():
    nbi = Data()

    # function to detect a link or a path on the local computer and return a df
    #df = nbi.getData('https://www.fhwa.dot.gov/bridge/nbi/2018/delimited/NE18.txt')
    
    #Set path of the csv here
    path = "" 

    # Set year of the csv here
    year_of_survey = 2018 

    df = pd.get_csv(path)
    df = nbi.renameDataColumns(df)
    df = nbi.dropIgnoredColumns(df)
    df = nbi.renameStateCodes(df)
    
    df['8: Structure Number'] = df['8: Structure Number'].str.strip()
    df['6A: Features Intersected'] = df['6A: Features Intersected'].str.strip("'").str.strip()
    df['7: Facility Carried By Structure'] = df['7: Facility Carried By Structure'].str.strip("'").str.strip()
    df['9: Location'] = df['9: Location'].str.strip("'").str.strip()
    df['16: Latitude'] = df['16: Latitude'].apply(str).apply(nbi.convertGeocoordinate)
    df['17: Longitude'] = df['17: Longitude'].apply(str).apply(nbi.convertGeocoordinate)
    df['39: Navigation Vertical Clearance'] = df['39: Navigation Vertical Clearance'] / 10
    df['40: Navigation Horizontal Clearance'] = df['40: Navigation Horizontal Clearance'] / 10
    
    df = nbi.createCaseName(df)
    df = nbi.createCaseId(df)
    #df = nbi.createYear(df)

    df['Year'] = year_of_survey

    df = nbi.createMaterialColumn(df)
    df = nbi.createConstructionTypeColumn(df)
    df.to_excel("processed NBI spreadsheet.xls", index = False)

    df = nbi.renameCols(df)
    df = nbi.rearrangeCols(df)
    df.to_csv("transformed NBI spreadsheet.csv", index = False)

if __name__ == '__main__':
    main()
