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
    
	def test_filter_and_sort_results_success(self):
        
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

		self.assertTrue('Tennis' in filtered_sorted_results)
		
		for i in  range(len(data["Tennis"])-1):
			self.assertGreater(
				datetime.strptime(filtered_sorted_results["Tennis"][i]['publicationDate'], '%b %d, %Y %I:%M:%S %p'),
				datetime.strptime(filtered_sorted_results["Tennis"][i+1]['publicationDate'], '%b %d, %Y %I:%M:%S %p')
			)
		
	def test_filter_and_sort_results_sort_only(self):
        
		data = {
			"Tennis": [
				{"publicationDate": "May 7, 2020 11:15:15 PM", "tournament": "Roland Garros"},
				{"publicationDate": "May 8, 2020 11:15:15 PM", "tournament": "Wimbledon"}
			],
			"f1Results": [
				{"publicationDate": "May 7, 2020 11:15:15 PM", "tournament": "Silverstone"},
				{"publicationDate": "May 11, 2020 11:15:15 PM", "tournament": "Silverstone"}
			]
		}
        
		sorted_results = filter_and_sort_results(data)
        
		# Assert the correct events are filtered and sorted
		self.assertEqual(len(sorted_results), 2)

		self.assertTrue('Tennis' in sorted_results)
		self.assertTrue('f1Results' in sorted_results)
		
		for i in  range(len(data["Tennis"])-1):
			self.assertGreater(
				datetime.strptime(sorted_results["Tennis"][i]['publicationDate'], '%b %d, %Y %I:%M:%S %p'),
				datetime.strptime(sorted_results["Tennis"][i+1]['publicationDate'], '%b %d, %Y %I:%M:%S %p')
			)
		for i in range(len(data["f1Results"])-1):
			self.assertGreater(
				datetime.strptime(sorted_results["Tennis"][i]['publicationDate'], '%b %d, %Y %I:%M:%S %p'),
				datetime.strptime(sorted_results["Tennis"][i+1]['publicationDate'], '%b %d, %Y %I:%M:%S %p')
			)
		
	def test_filter_and_sort_results_no_input(self):
		with self.assertRaises(Exception) as context:
			filter_and_sort_results({})
		self.assertTrue('unexpected empty input parameter results' in  repr(context.exception))

	def test_filter_and_sort_results_invalid_event(self):
		data = {
			"Tennis": [
				{"publicationDate": "May 7, 2020 11:15:15 PM", "tournament": "Roland Garros"},
				{"publicationDate": "May 8, 2020 11:15:15 PM", "tournament": "Wimbledon"}
			],
			"f1Results": [
				{"publicationDate": "May 7, 2020 11:15:15 PM", "tournament": "Silverstone"}
			]
		}
        
		# Filter and sort for Football
		event_types = ["Football"]
		filtered_sorted_results = filter_and_sort_results(data, event_types)
		self.assertEqual(len(filtered_sorted_results), 0)


if __name__ == '__main__':
    unittest.main()
