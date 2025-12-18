import requests

with open('.token', 'r') as f:
    tkn = f.read()

results = []
for i in range(1,11):
    url = "https://api.github.com/search/code?q=x-sparql-anything+in:file&per_page=100&page="+str(i)

    headers = {
    'Authorization': tkn.strip()
    }

    response = requests.request("GET", url, auth=('enridaga', tkn.strip())).json()
    try:
        #print(len(response['items']))
        results.append(response)
    except:
        print("ERROR = ", response)

import json
with open('results.json', 'w') as fp:
    json.dump(results, fp)