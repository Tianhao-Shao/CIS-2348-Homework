import csv
import datetime

ManufacturerList = []
PriceList = []
ServiceDatesList = []

# open each file and write into each list
with open('ManufacturerList.csv', 'r') as f1:
    Manufacturer_List = csv.reader(f1)
    for row in Manufacturer_List:
        ManufacturerList.append(row)

with open('PriceList.csv', 'r') as f2:
    Price_List = csv.reader(f2)
    for row in Price_List:
        PriceList.append(row)

with open('ServiceDatesList.csv', 'r') as f3:
    ServiceDates_List = csv.reader(f3)
    for row in ServiceDates_List:
        ServiceDatesList.append(row)

# 1) a.
# making FullInventory list for FullInventory.cvs
FullInventory = ManufacturerList

for row in FullInventory:
    for row2 in PriceList:
        if row[0] == row2[0]:
            row.insert(3, row2[1])
    for row3 in ServiceDatesList:
        if row[0] == row3[0]:
            row.insert(4, row3[1])

# sorting FullInventory list by company name
FullInventory = sorted(FullInventory, key=lambda x: x[1])

# output FullInventory.cvs file
with open('FullInventory.csv', 'w') as f:
    for row in FullInventory:
        Full_Inventory = csv.writer(f)
        Full_Inventory.writerow(row)

# 1) b.

Inventory = FullInventory
PhoneInventory = []
LaptopInventory = []
TowerInventory = []

# Phone
for row in Inventory:
    if row[2] == 'phone':
        PhoneInventory.append(row)

FullInventory = sorted(FullInventory, key=lambda x: x[0])

with open('PhoneInventory.csv', 'w') as f:
    for row in PhoneInventory:
        PhoneInventory = csv.writer(f)
        PhoneInventory.writerow(row)
# laptop
for row in Inventory:
    if row[2] == 'laptop':
        LaptopInventory.append(row)

LaptopInventory = sorted(LaptopInventory, key=lambda x: x[0])

with open('LaotopInventory.csv', 'w') as f:
    for row in LaptopInventory:
        LaptopInventory = csv.writer(f)
        LaptopInventory.writerow(row)

# tower
for row in Inventory:
    if row[2] == 'tower':
        TowerInventory.append(row)

TowerInventory = sorted(TowerInventory, key=lambda x: x[0])

with open('TowerInventory.csv', 'w') as f:
    for row in TowerInventory:
        TowerInventory = csv.writer(f)
        TowerInventory.writerow(row)

# 1) c.

ServiceDateInventory = FullInventory

PastServiceDateInventory = []

today = datetime.datetime.now()
today = today.strftime('%m/%d/%Y')
today = datetime.datetime.strptime(today, '%m/%d/%Y').date()

for row in ServiceDateInventory:
    d = row[4]
    d = datetime.datetime.strptime(d, '%m/%d/%Y').date()
    if d < today:
        PastServiceDateInventory.append(row)

PastServiceDateInventory = sorted(PastServiceDateInventory, key=lambda x: datetime.datetime.strptime(x[4].rsplit(None, 1)[-1], '%m/%d/%Y'))
with open('PastServiceDateInventory.csv', 'w') as f:
    for row in PastServiceDateInventory:
        PastServiceDateInventory = csv.writer(f)
        PastServiceDateInventory.writerow(row)

# 1) d.
Damaged_Inventory = Inventory
DamagedInventory = []

for row in Damaged_Inventory:
    if row[5] == 'damaged':
        DamagedInventory.append(row)

with open('DamagedInventory.csv', 'w') as f:
    for row in DamagedInventory:
        DamagedInventory = csv.writer(f)
        DamagedInventory.writerow(row)






