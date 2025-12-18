import json
with open('results.json', 'r') as fp:
    data = json.load(fp)

with open('.token', 'r') as f:
    tkn = f.read()

urls = []
x = 1
for p in data:
    if 'items' not in p:
        continue
    print(x, len(p['items']))
    x = x + 1
    for r in p['items']:
        url = r['url']
        print(url)
        # Only keep .rq and .sparql
        if r['html_url'].endswith('.rq') or r['html_url'].endswith('.sparql'):
            urls.append(url)

print(len(urls), " urls")

# Download
import requests
import os
x = 0
for url in urls:
    x = x + 1
    comment = f"# {url}\n"
    print("doing ", comment)
    j = requests.request("GET", url , auth=('enridaga', tkn.strip())).json()
    fname = "query-" + str(x) + ".rq"
    if os.path.exists(fname):
        continue
    try:
        download_url = j['download_url']
        output = requests.request("GET", download_url, auth=('enridaga', tkn.strip())).content.decode('utf-8')
        with open('queries/' + fname, 'w') as fp:
            fp.write(comment + output)
    except Exception as e:
        print ("An error occurred")
        print (j)

