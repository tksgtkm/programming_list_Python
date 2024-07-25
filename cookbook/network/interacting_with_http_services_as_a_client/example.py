import json
from pprint import pprint
from urllib import request, parse

url = 'http://httpbin.org/get'

parms = {
    'name1': 'value1',
    'name2': 'value2'
}

querystring = parse.urlencode(parms)

u = request.urlopen(url + '?' + querystring)
resp = u.read()

json_resp = json.loads(resp.decode('utf-8'))
pprint(json_resp)