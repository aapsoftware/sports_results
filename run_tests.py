import unittest
from  datetime import datetime
from get_sports_data import fetch_results, filter_and_sort_results, API_URL

class TestFetchResults(unittest.TestCase):
    
	def test_fetch_results_is_succesful(self):
        
		result = fetch_results(API_URL, "en")
		self.assertIsInstance(result, dict)

	def test_fetch_results_invalid_url(self):
		with self.assertRaises(Exception) as context:
			API_URL = "n/a"
			result = fetch_results(API_URL)
			
		self.assertTrue('Error fetching API results' in  repr(context.exception))

	def test_fetch_results_wrong_url(self):
		with self.assertRaises(Exception) as context:
			API_URL = "https://www.google.com"
			result = fetch_results(API_URL)
			
		self.assertTrue('Api call returned unexpected status' in  repr(context.exception))

	def test_fetch_results_default_params(self):
		result = fetch_results()
		self.assertIsInstance(result, dict)

	def test_fetch_results_different_locales(self):
		result = fetch_results(locale="en")
		self.assertIsInstance(result, dict)
		
		result = fetch_results(locale="de")
		self.assertIsInstance(result, dict)

		result = fetch_results(locale="fr")
		self.assertIsInstance(result, dict)

		result = fetch_results(locale="es")
		self.assertIsInstance(result, dict)

	def test_fetch_results_invalid_locale(self):
		result = fetch_results(locale="this_is_wrong")
		self.assertIsInstance(result, dict)
    
	def test_filter_and_sort_results(self):
        
		data = {
			"Tennis": [
				{"publicationDate": "May 7, 2020 11:15:15 PM", "tournament": "Roland Garros"},
				{"publicationDate": "May 8, 2020 11:15:15 PM", "tournament": "Wimbledon"}
			],
			"f1Results": [
				{"publicationDate": "May 7, 2020 11:15:15 PM", "tournament": "Silverstone"}
			]
		}
        
		# Filter and sort for Tennis
		event_types = ["Tennis"]
		filtered_sorted_results = filter_and_sort_results(data, event_types)
        
		# Assert the correct events are filtered and sorted
		self.assertEqual(len(filtered_sorted_results), 1)
		print(filtered_sorted_results)
		self.assertTrue('Tennis' in filtered_sorted_results)
		
		for i in  range(len(data["Tennis"])-1):
			self.assertLess(
				datetime.strptime(data["Tennis"][i]['publicationDate'], '%b %d, %Y %I:%M:%S %p'),
				datetime.strptime(data["Tennis"][i+1]['publicationDate'], '%b %d, %Y %I:%M:%S %p')
			)
		#self.assertEqual(filtered_sorted_results['Tennis'][0]['tournament'], "Roland Garros")

if __name__ == '__main__':
    unittest.main()
