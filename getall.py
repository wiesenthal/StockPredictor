import requests

r = requests.get("https://datafied.api.edgar-online.com/v2/companies?companynames=*&limit=22136&appkey=842d5fe207af6c02fa4a0387a9b025a5")

data = r.json();
for i in range(len(data["result"]["rows"])):
    for j in range(len(data['result']['rows'][i]['values'])):
        if data['result']['rows'][i]['values'][j]['field'] == 'entityid':
                 print(data['result']['rows'][i]['values'][j]['value'])
