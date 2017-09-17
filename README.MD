Using the NIMH Data Archive search API perform the following tasks
==================================================================

# Problem 1:

Using the 'full' search operation from the search API, identify the data elements scoring > 0.33 for an arbitrary query term (i.e., depression) that include the query term in the description and/or notes field. To complete this and subsequent problems I should be able to use any query phrase.

You should use the nda_sw_removal index for this search, and the type should be dataelement. 

The search API endpoint is https://ndar.nih.gov/api/search.  To execute a search using the full search operation for the dataelement type you should POST your query phrase.

You can explore the API in your browser using the attached swagger interface located at https://ndar.nih.gov/api/search

NOTES:
- The return type for dataelement search is labelled as datadict.
- Each search result type includes a count for the total number of search hits, but the default number of results to return is 5 and is controlled by the size query parameter.

## Here is sample code for executing the search in Python:

import requests
import json

query_phrase = 'depression'

r = requests.post('https://ndar.nih.gov/api/search/nda_sw_removal/dataelement/full?size=5',
                  headers={'Accept':'application/json'},
                  data= query_phrase)
                  
search_results = json.loads(r.text)
data_elements = search_results['datadict']

print(data_elements)

# Problem 2:

For data elements meeting the search criteria in Problem 1 (score > 0.33 with query phrase in notes and/or description), calculate total subjectCount from data structures containing those data elements and least each data structure with its count.

NOTES: 
- The data structures should be unique (i.e., if a dataStructure shows up more than once, you should only list it once).
- The data structures should only be counted towards the total subjectCount once.

# Problem 3:

Using the data dictionary API, list the latest change for each data element and each data structure.

The data dictionary API is https://ndar.nih.gov/api/datadictionary/v2/

You can explore the API interactively using the swagger interface at https://ndar.nih.gov/swagger/

You should be using the GET HTTP method and the following URLs to solve this problem:

GET https://ndar.nih.gov/api/datadictionary/v2/datastructure/{shortName}/changes

GET https://ndar.nih.gov/api/datadictionary/v2/dataelement/{elementName}/changes



