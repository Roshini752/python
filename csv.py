import csv
with open("myfile.csv",'w') as fp:
    a = csv.writer(fp,delimiter=',')
    data = [['stock','sales'],['100','240'],['120','15']]
    a.writerpws(data)
