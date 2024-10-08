# Task statement
Use the following API to retrieve sports results and sort into a table of results that are displayed in the CLI. Each sport result contains several data and always includes the publication time. 
    Method: POST
    Content-Type: application/json
    Url: https://restest.free.beeceptor.com/results 
Tasks:
-	Create python script that displays the sports results in reverse chronological order in the CLI.
-	Add an argument to the script to display only certain types or events (e.g. f1Results)
-	Add an argument to set the locale (e.g. en)
-	How can you confirm the code works?
-	Bonus: Implement the rest call asynchronously


# Solution
	The get_sports_data.py script fetches data from the https://restest.free.beeceptor.com/results API and prints the output in json format in reverse chronological order
	
	usage: get_sports_data.py [-h] [-e [EVENTS]] [-l [LOCALE]]

	optional arguments:
  	-h, --help            show this help message and exit
  	-e [EVENTS], --events [EVENTS]
                        	comma separated string of event types e.g. 'Tennis'
  	-l [LOCALE], --locale [LOCALE]
                        	request locale e.g. en, fr, de, etc.

	Running the code:
	Download the code, navigate to the parent directory and run one of the following:
		python3 get_sports_data/py
		OR
		./get_sports_data.py

	To run the async version of the code follow the steps below:
		Download the code and navigate to the parent directory
		install the python modules aiohttp and asyncio:
			pip3 install aiohttp, asyncio
		run the code:
			./get_sports_data_async.py
	

# Run the tests
	There are a number of test cases provided which exercise the code
	Unit tests can be run by running the following command:  
		python3 -m unittest run_tests.py
	Integration tests which exersize the sync and async version of the script can be run by running the following command:
		python3 -m unittest run_integration_tests.py
