import json
import urllib.request

url = 'https://raw.githubusercontent.com/ItaengaConecta/libic-data/main/json/libic-textos-exatas.json'

data = urllib.request.urlopen(url)
dw = data.read()

data_json = json.loads(dw.decode())
for i in data_json:
    print('\n{} \n\n{}\n{}'.format(10*'-', i['Title'],i['MainLink']))
print('\nend...')
