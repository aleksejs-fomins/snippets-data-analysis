import json
from pprint import pprint

with open('stickman-edge-templates/test.json') as f:
    data = json.load(f)

pprint(data)
