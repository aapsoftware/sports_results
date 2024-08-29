import unittest
from  datetime import datetime
import subprocess
import json

class TestIntegration(unittest.TestCase):
    
    def check_script_default_output(self, results):
       
		# Check if the output contains expected results
        self.assertIn("Tennis", results)
        self.assertIn("nbaResults", results)
        self.assertIn("f1Results", results)
        
        self.assertEqual(len(results['Tennis']), 3)
        self.assertEqual(len(results['nbaResults']), 5)
        self.assertEqual(len(results['f1Results']), 3)
        
        # Check is output is in reverse chronological order
        for i in  range(len(results["Tennis"])-1):
            self.assertGreater(
                datetime.strptime(results["Tennis"][i]['publicationDate'], '%b %d, %Y %I:%M:%S %p'),
                datetime.strptime(results["Tennis"][i+1]['publicationDate'], '%b %d, %Y %I:%M:%S %p')
			)
        for i in range(len(results["nbaResults"])-1):
            self.assertGreater(
				datetime.strptime(results["nbaResults"][i]['publicationDate'], '%b %d, %Y %I:%M:%S %p'),
				datetime.strptime(results["nbaResults"][i+1]['publicationDate'], '%b %d, %Y %I:%M:%S %p')
			)
        for i in  range(len(results["f1Results"])-1):
            self.assertGreater(
				datetime.strptime(results["f1Results"][i]['publicationDate'], '%b %d, %Y %I:%M:%S %p'),
				datetime.strptime(results["f1Results"][i+1]['publicationDate'], '%b %d, %Y %I:%M:%S %p')
			)
		
        
    def check_script_filter_output(self, results):
       
        # Check if the output contains expected results    
        self.assertIn("Tennis", results)
        self.assertNotIn("nbaResults", results)
        self.assertNotIn("f1Results", results)
        
        self.assertEqual(len(results['Tennis']), 3)
            
        # Check is output is in reverse chronological order
        for i in  range(len(results["Tennis"])-1):
            self.assertGreater(
                datetime.strptime(results["Tennis"][i]['publicationDate'], '%b %d, %Y %I:%M:%S %p'),
                datetime.strptime(results["Tennis"][i+1]['publicationDate'], '%b %d, %Y %I:%M:%S %p')
            )
            
    def check_script_no_output(self, results):
        # Check if the output is empty dict    
        self.assertEqual({}, results)
        
 ################### run tests using sync script ###############################      
    def test_script_output(self):
        # Run the script with specific arguments and capture output
        result = subprocess.run(
            ['python3', 'get_sports_data.py'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Check if the output contains expected results
        results = json.loads(result.stdout)
        self.check_script_default_output(results)
 
    def test_script_output_different_locales(self):
        # Run the script with locale
        result = subprocess.run(
            ['python3', 'get_sports_data.py', '-l', 'en'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Check if the output contains expected results
        results = json.loads(result.stdout)
        self.check_script_default_output(results)
        
        # Run the script with locale
        result = subprocess.run(
            ['python3', 'get_sports_data.py', '-l', 'de'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Check if the output contains expected results
        results = json.loads(result.stdout)
        self.check_script_default_output(results)
        
        # Run the script with locale
        result = subprocess.run(
            ['python3', 'get_sports_data.py', '-l', 'fr'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Check if the output contains expected results
        results = json.loads(result.stdout)
        self.check_script_default_output(results)
        
    
    def test_script_filter_output(self):
        
        result = subprocess.run(
            ['python3', 'get_sports_data.py', '-e', 'Tennis'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Check if the output contains expected results
        results = json.loads(result.stdout)    
        self.check_script_filter_output(results)
        
    def test_script_invalid_filter_output(self):
        
        result = subprocess.run(
            ['python3', 'get_sports_data.py', '-e', 'none'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Check if the output contains expected results
        results = json.loads(result.stdout)    
        self.check_script_no_output(results)
        
################### run tests using async script ###############################  
    
    def test_script_output_async(self):
        # Run the script with specific arguments and capture output
        result = subprocess.run(
            ['python3', 'get_sports_data_async.py'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
            )
   
        # Check if the output contains expected results
        results = json.loads(result.stdout)
        self.check_script_default_output(results)
              
    def test_script_output_different_locales_async(self):
        # Run the script with locale
        result = subprocess.run(
            ['python3', 'get_sports_data_async.py', '-l', 'en'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
      
        # Check if the output contains expected results
        results = json.loads(result.stdout)
        self.check_script_default_output(results)
      
        # Run the script with locale
        result = subprocess.run(
            ['python3', 'get_sports_data_async.py', '-l', 'de'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
      
        # Check if the output contains expected results
        results = json.loads(result.stdout)
        self.check_script_default_output(results)
      
        # Run the script with locale
        result = subprocess.run(
            ['python3', 'get_sports_data_async.py', '-l', 'fr'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
      
        # Check if the output contains expected results
        results = json.loads(result.stdout)
        self.check_script_default_output(results)
      
  
        def test_script_filter_output_async(self):
      
            result = subprocess.run(
                ['python3', 'get_sports_data_async.py', '-e', 'Tennis'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
      
            # Check if the output contains expected results
            results = json.loads(result.stdout)    
            self.check_script_filter_output(results)
      
        def test_script_invalid_filter_output_async(self):
      
            result = subprocess.run(
                ['python3', 'get_sports_data_async.py', '-e', 'none'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
      
            # Check if the output contains expected results
            results = json.loads(result.stdout)    
            self.check_script_no_output(results)
        
if __name__ == '__main__':
    unittest.main()
