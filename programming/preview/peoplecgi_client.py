from urllib.request import urlopen

url = 'http://localhost:8080/cgi-bin/peoplecgi.py?action=Fetch&key=takumi'

print(urlopen(url).read())