import json

kd_stats = 'C:/Users/greg6750/Documents/IPython Notebooks/NBAproject/kd.json'

with open(kd_stats) as data_file:
    data = json.load(data_file)

print('Columns of the Data')
print(data['resultSets'][0]['headers'])

print('Game Stats')
for row in data['resultSets'][0]['rowSet']:
    print(row)