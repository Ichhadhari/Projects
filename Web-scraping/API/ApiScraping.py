#https://www.topuniversities.com/sites/default/files/qs-rankings-data/en/3751069.txt?rs7x3o

import httpx
import pandas as pd
import json
from rich import print

def download_json(url):
    resp = httpx.get(url)

    for node in resp.json()["data"]:
        yield node

def save_to_json(data):
    with open('results.json', 'w') as f:
        json.dump(data, f)

def save_to_csv(data):
    df = pd.DataFrame(data)
    df.to_csv('results.csv', index=False)

def main():
    url = "https://www.topuniversities.com/sites/default/files/qs-rankings-data/en/3751069.txt?rs7x3o"
    results =[]
    for item in download_json(url):
        results.append(item)

    print(len(results))
    save_to_json(results)
    save_to_csv(results)

if __name__=="__main__":
    main()