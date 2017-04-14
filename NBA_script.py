
import json
kd_stats = 'C:/PythonforGIS/NBA_PROJECT/kd.json'

with open(kd_stats) as data_file:
data = json.load(data_file)

for row in data['resultSets'][0]['rowSet']:
print(row)