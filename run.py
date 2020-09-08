import json
import sys
import requests
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

if(len(sys.argv) == 1):
    print("Please specify route")
    exit()

with open('routes/'+sys.argv[1]+'.json') as f:
  data = json.load(f)

#Variables
TotalPing = 0

for i in range(0, data['times']):
    # Send request
    response = requests.post(data["url"], json=data["body"], verify=False)
    if(response.status_code == 200):
        TotalPing = TotalPing + response.elapsed.total_seconds()*1000

print("Took "+str(round(TotalPing))+"ms to complete "+str(data['times'])+" requests. Average time was "+str(round(TotalPing/data['times']))+"ms")