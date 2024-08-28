#!/usr/bin/python3
 
'''
Doctoring tbd
'''

import sys
if not sys.version_info >= (3, 5):
	major_version = sys.version_info.major
	minor_version = sys.version_info.minor
	micro_version = sys.version_info.micro
	print(f"you are using python {major_version}.{minor_version}.{micro_version} and minimum 3.5 is required")
	
import aiohttp
import asyncio
import requests
from  datetime import datetime
import argparse

import json

API_URL = "https://restest.free.beeceptor.com/results"

def check_python_version():
    """Ensure the script is running on Python 3.5 or higher."""

    if not sys.version_info >= (3, 5):
        major_version = sys.version_info.major
        minor_version = sys.version_info.minor
        micro_version = sys.version_info.micro
        sys.exit(f"Error: You are using Python {major_version}.{minor_version}.{micro_version}. "
                 f"Minimum version required is 3.5.")

def fetch_results(locale:str) -> dict:
	"""Fetch results from the API with the specified locale."""

	headers = {
        	"Accept-Language": locale,
        	"Content-Type": "application/json"
    	}
	
	results = {}
	try:
		response = requests.post(API_URL, headers=headers)
		if response.status_code == 200:
			results = response.json()
		else:
			print(f"Api call returned unexpected status: {response.status_code}")
	except requests.exceptions.RequestException as e:
        	raise(f"Error fetching results: {e}")
	
	return results

def filter_and_sort_results(results: dict, event_types: list[str] = None) -> dict:
	"""Filter and sort the sport events data."""
	if not results:
		raise ValueError(f"unexpected empty input parameter results")

	filtered_results = results
    
	if event_types:
		filtered_results = {key: value for key, value in filtered_results.items() if key in event_types}
		
	if filtered_results:
		for k, v in filtered_results.items():
			filtered_results[k] = sorted(v, key=lambda x: datetime.strptime(x['publicationDate'], '%b %d, %Y %I:%M:%S %p'), reverse=True)

	return filtered_results

def main(event_types: list[str] = None, locale: str = None): 
	results = fetch_results(locale)
        
	sorted_filtered_results = filter_and_sort_results(results, event_types)


	print(json.dumps(
		sorted_filtered_results,
		sort_keys=True,
		indent=4,
		separators=(',',':')
		)
	)
	

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-e", "--events", nargs="?", help="comma separated string of event types")
	parser.add_argument("-l", "--locale", nargs="?", help="request locale e.g. en, fr, de, etc.")
	args = parser.parse_args()
	
	event_types = []
	
	if args.events:
		event_types = [event for event in args.events.split(",")]
	
	locale = args.locale if args.locale else "en"
		

	
	main(event_types, locale)