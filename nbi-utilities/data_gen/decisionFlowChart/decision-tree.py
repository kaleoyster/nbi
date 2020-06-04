"""
Decision - tree with a selction of replacements, rehabs, and redecks
"""
import csv
import pandas as pd
import requests
import io

class Flow():
    def __init__(self):
        """
          Contains a set of conditions
        """

    def condition_1_1(self, df):
        """ 

        """
        if df['Pile Condition'] < 3:
            return True
        else:
            return False

    def condition_2_1(self, df):
        if condition1_1(self, df) == False:
            if df['Timber Pile'] == T:
                return True
            else:
                return False
        else:
            return False

    def condition_3_1(self, df):
        "Returns a pandas dataframe that satisifies the condition 3.1, returns True if the bridge qualifies for replacement  "
     #   if df['SUBSTRUCTURE_COND_060'] < 3:
     #       return True
     #   else:
     #       return False
        df = df[~df['SUBSTRUCTURE_COND_060'].isin(['N'])]
        df['SUBSTRUCTURE_COND_060'] = df['SUBSTRUCTURE_COND_060'].astype(int)
        return df[df['SUBSTRUCTURE_COND_060'] < 3]

    def condition_4_1(self, df):
        if condition_1_1(self, df) and condition_2_1(self, df) and condition_3_1(self, df) == False:
            if df['Scour Critical'] < 3:
                return True
            else:
                return False
        else:
            return False

    def condition_4_2(self, df):
        if condition_1_1(self, df) and condition_2_1(self, df) and condition_3_1(self, df) == False:
            if df['Scour Critical']  == 8:
                return True
            else:
                return False
        else:
            return False

    def HydrologyReviewMitigateScour(self, df):
        pass

    def condition_5_1(self, df):
        if HydrologyReviewMitigateScour(self, df) == True:
            return True
        else:
            return False

    def condition_5_2(self, df):
        if HydrologyReviewMitigateScour(self, df) == False:
            return True
        else:
            return False

    def condition_6_1(self, df):
        if df['Age'] > 75:
            return True
        else:
            return False

    def condition_7(self, df):
        if condition_1_1(self, df) and condition_2_1(self, df) and condition_3_1(self, df) and condition_6_1(self, df) == False:
            if df['Age'] <= 75:
                return True
            else:
                return False

    def repairSubstructureFeasibile(self, df):
        pass

    def condition_8(self, df):
        if repairSubstructureFeasible(self, df) == False:
            return True
        else:
            return False

    def condition_8_1(self, df):
        if repairSubstructureFeasible(self, df) == True:
            return True
        else:
            return False

    def condition_9_1(self, df):
        if p&h > 0: 
            return True
        else:
            return False

    def condition_9_2(self, df):
        if frac_crtit != 0:
            return True
        else:
            return False

    # There may be some of the deadzones
    # Cover the deadzones in the driver program

    def condition_10_1(self, df):
        if df['Age'] > 75:
            return True
        else:
            return False

    def condition_11_1(self, df):
        if df['Age'] < 75:
            if df['Design Load'] >= HS15:
                return True
            else:
                return False

    def condition_12_1(self, df):
        ## 12.1 occurs only if 1.1, 2.1, 3.1, 6.1, 10.1 = OK
        ## 4.1, or 4.2, and 7.0
        if df['Age'] < 75:
            if df['Design Load'] < HS15:
                return True
            else:
                return False

    def condition_13_1(self, df):
        if rehabPendingSubCapacityReview == False:
            return True
        else:
            return False

    def condition_13_2(self, df):
        if rehabPendingSubCapacityReview == True:
            return True
        else:
            return False

#    def condition_16_2(self, df):
#        if condition_1_1(self, df) and condition_2_1(self, df) and condition_3_1(self, df) and condition_6_1(self, df) and condition_9_1(self, df) and condition_9_2(self, df) and condition_14_1(self, df) and condition_15_1(self, df) and condition_4_1(self, df) and condition_4_2(self, df) and condition_7_0(self, df) == False:
#           if df['deck'] > 5:
#                return True
#           else:
#                return False
#        else:
#            False
#    
#    def condition_14_1(self, df):
#        if condition_1_1(self, df) and condition_2_1(self, df) and condition_3_1(self, df)and condition_6_1(self, df) and condition_9_1(self, df)  and condition_9_2(self, df) == False:
#            if df['Deck'] < 4:
#                  return True
#              else:
#                  return False
#        else:
#            False
#      
#    def condition_15_1(self, df):
#        if condition_1_1(self, df) and condition_2_1(self, df)  and condition_3_1(self, df) and condition_6_1(self, df) and condition_9_1(self, df) and condition_9_2(self, df) and condition_14_1(self, df) or condition_14_2(self, df) and condition_7_0(self, df) == False:
#              if df['Asphalt 108'] != 6:
#                  return True
#              else:
#                  return False
#          else:
#              False
#
#    def condition_16_1(self, df):
#        if condition_1_1(self, df) and condition_2_1(self, df) and condition_3_1(self, df) and condition_6_1(self, df) and condition_9_1(self, df) and condition_9_2(self, df) and condition_14_1(self, df) and condition_15_1(self, df) and condition_4_1(self, df) and condition_4_2(self, df) and condition_7_0(self, df) == False:
#                if df['Asphalt'] ==  6:
#                    return True
#                else:
#                    return False
#            else:
#                False
#
#def main():
#    maintain = Flow()
#    
#    # data path
#    data_path = 'ne18.csv'
#    
#    # Creating DataFrame 
#    df = pd.read_csv(data_path)
#    
#    # Change the column names of the dataframe
#    
#    # filter data that qualify for condition 3_1
#    df_3_1 = maintain.condition_3_1(df) 
#    print(df_3_1)
#    
#
#if  __name__ == '__main__':
#    main()













        





