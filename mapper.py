import os
import json

with open(os.path.join('table-legacy.json')) as file:
  fileInDict = json.loads(file.read())
  normalized = []

  for item in fileInDict['data']:
    item = {
      'id': item['id'],
      'description': item['descricao'],
      'priceInCents': int((item['valor'] * 100)),
      'costInCents': int(((item['valor'] * 100) / 2)),
      'amount': 1
    }
    normalized.append(item)
  
  newFile = open(os.path.join('table-current.json'), 'w')
  data = {'data': normalized}
  newFile.write(json.dumps(data, ensure_ascii=False))