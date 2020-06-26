import sys
import requests

APPKEY = '842d5fe207af6c02fa4a0387a9b025a5'
URL="https://datafied.api.edgar-online.com/v2/corefinancials/qtr.json"
period='2020q1'
period=str(sys.argv[1])
limit='22136'
fields=['totalrevenue','commonstock','totalassets','totalliabilities','netincome','cashandcashequivalents', 'totalstockholdersequity', 'primarysymbol','periodenddate']
fields.sort()
field_len = len(fields)

z = 0

for i, field in enumerate(fields):
    print(field, end="")
    if i < len(fields) - 1:
        print("\t", end="")
print()
#open file of ids
f = open('every3.txt', 'r')
idlist=f.read().splitlines()
idlistlen = len(idlist)
gap=2000
inactivecompanies = 0
for indy in range(0, 23000, gap):
    ids=""
    start = indy
    end = indy + gap
    for i in range(start, end):
        if i < idlistlen:
            ids+=idlist[i] + ","
    ids = ids[:-1]
    
    PARAMS={'entityids':ids,'sortby':'companyname,fiscalperiod desc','fiscalperiod':period,'limit':limit,'appkey':APPKEY}
    r = requests.get(url=URL,params=PARAMS);
    data = r.json()
    for x in range(len(data["result"]['rows'])):
        field_list = []
        for i in range(len(data["result"]['rows'][x]['values'])):
            if data["result"]['rows'][x]['values'][i]['field'] in fields:
                field_list.append((data["result"]['rows'][x]['values'][i]['field'],str(data["result"]['rows'][x]['values'][i]['value'])))
        field_list = sorted(field_list, key=lambda x: x[0])
        j = 0
        if len(field_list) == field_len:
            print ("\t".join(y[1] for y in field_list))

        #for field in fields:
        #    if j < len(field_list) and field == field_list[j][0]:
        #        print(field_list[j][1], end="")
        #        j+=1
        #    else:
        #        print("NaN", end="")
        #    if j < len(fields):
        #        print("\t", end="")
        #    if j >= len(fields):
        #        break
        #print()
    z += x
f.close()
