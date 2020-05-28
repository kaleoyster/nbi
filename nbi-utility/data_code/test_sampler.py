from unittest import TestCase
import sampler 

PATH = ""
class TestSample(unittest.TestCase):

      def test_sampler():
          sampler = sampler.sampler
          sample_df = pd.DataFrame({'Fruits':['Apple', 'Banana', 'Chiku', 'Orange', 'Peru'],
                                    'Price': [2, 1, 1.5, 2.1, 3]})
          
          sampler(sample_df, 'sample1.csv')
          test_sample = pd.read_csv(PATH)
          self.assertEquals(samplw_df, test_sample)  

if __name__ == "__main__":
    unittest.main()
