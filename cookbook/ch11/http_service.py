from urllib import request, parse

url = 'http://httpbin.org/get'

parms = {
    'name1': 'value1',
    'name2': 'value2'
}

querystring = parse.urlencode(parms)

u = request.urlopen(url + '?' + querystring)
resp = u.read()

import json
from pprint import pprint

json_resp = json.loads(resp.decode('utf-8'))
pprint(json_resp)