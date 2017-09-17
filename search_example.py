import requests
import json

query_phrase = 'depression'

r = requests.post('https://ndar.nih.gov/api/search/nda_sw_removal/dataelement/full?size=5',
                  headers={'Accept':'application/json'},
                  data= query_phrase)
search_results = json.loads(r.text)
data_elements = search_results['datadict']
print(data_elements)
