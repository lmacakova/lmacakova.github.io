import requests
import json

# first I found this link
cso = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"
# GET request to the API endpoint
response = requests.get(cso)
exchequer_data=response.json()
with open("cso.json", "w") as f: # printed and stored
        f.write(response.text)
        