import json
from datetime import datetime
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import numpy as np

kd_stats = 'C:/PythonforGIS/NBA_Project/kd.json'
sc_stats = 'C:/PythonforGIS/NBA_Project/sc.json'
dg_stats = 'C:/PythonforGIS/NBA_Project/dg.json'
kt_stats = 'C:/PythonforGIS/NBA_Project/kt.json'

with open(kd_stats) as data_file:
    kddata = json.load(data_file)

with open(sc_stats) as data_file:
    scdata = json.load(data_file)

with open(dg_stats) as data_file:
    dgdata = json.load(data_file)

with open(kt_stats) as data_file:
    ktdata = json.load(data_file)


print('Columns of the Data')
print(kddata['resultSets'][0]['headers'])

print('Game Stats')
kd_buckets = []
kd_gamedates = []

for row in kddata['resultSets'][0]['rowSet']:
    print(str(row[24]) + " Points scored on " + row[3])
    print(datetime.strptime(row[3], '%b %d, %Y'))
    kd_buckets.append(row[24])
    kd_gamedates.append(datetime.strptime(row[3], '%b %d, %Y'))


print('Game Stats')
sc_buckets = []
sc_gamedates = []

for row in scdata['resultSets'][0]['rowSet']:
    print(str(row[24]) + " Points scored on " + row[3])
    print(datetime.strptime(row[3], '%b %d, %Y'))
    sc_buckets.append(row[24])
    sc_gamedates.append(datetime.strptime(row[3], '%b %d, %Y'))


print('Game Stats')
dg_buckets = []
dg_gamedates = []


for row in dgdata['resultSets'][0]['rowSet']:
    print(str(row[24]) + " Points scored on " + row[3])
    print(datetime.strptime(row[3], '%b %d, %Y'))
    dg_buckets.append(row[24])
    dg_gamedates.append(datetime.strptime(row[3], '%b %d, %Y'))


print('Game Stats')
kt_buckets = []
kt_gamedates = []


for row in ktdata['resultSets'][0]['rowSet']:
    print(str(row[24]) + " Points scored on " + row[3])
    print(datetime.strptime(row[3], '%b %d, %Y'))
    kt_buckets.append(row[24])
    kt_gamedates.append(datetime.strptime(row[3], '%b %d, %Y'))

x = mdates.date2num(sc_gamedates)
regression = np.polyfit(x,sc_buckets,1)
p4 = np.poly1d(regression)
print(regression)

xx = np.linspace(x.min(), x.max(), 100)
dd = mdates.num2date(xx)

plt.figure(1)
##plt.plot(kd_gamedates,kd_buckets, 'b-o', label='kevin durant')
plt.plot(sc_gamedates,sc_buckets, 'ro', label='stephen curry')
##plt.plot(dg_gamedates,dg_buckets, 'y-o', label='dragmond green')
##plt.plot(kt_gamedates,kt_buckets, 'g-o', label='klay thompson')

plt.plot(dd, p4(xx), '-r')
plt.legend()
plt.show()