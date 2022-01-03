import os
import fnmatch
import csv
import itertools

L=[]

attrGen = '5 rounds floor 3_1'
fvGen = '5 rounds floor 3_3'
saveAs = '5rf33.csv'
L=sorted(L)

def merge1(L1,L2):
    lenL1 = len(L1)
    lenL2 = len(L2)
    print lenL1,lenL2
    i = 0
    j = 0
    L3 = []
    while j<lenL2 and i<lenL1:
        #print i,j
        if L1[i] == L2[j][1]:
            i +=1
            j +=1
        elif L1[i] < L2[j][1]:
            i +=1
        else:
            L1.append(L2[j][1])
            j +=1
    while j<lenL2:
        L1.append(L2[j][1])
        j +=1
    return L1         

#with open('extracted.csv', 'w') as out_file:
 #               	writer = csv.writer(out_file)
  #                      writer.writerow(tuple(temp))

for dirpath, dirs, files in os.walk(attrGen):
    for filename in fnmatch.filter(files, '*.txt'):
         print filename
         with open(os.path.join(dirpath, filename)) as in_file:
                stripped = (line.strip() for line in in_file)
    		lines = (line for line in stripped if line)
    		grouped = zip(*[lines] * 6)
    		gro = grouped[1:len(grouped)]
    		gro = sorted(gro, key=lambda tup:tup[1])
    		L = sorted(merge1(L,gro))


with open(saveAs, 'w') as out_file:
                	writer = csv.writer(out_file)
                        writer.writerow(tuple(L+['location']))


L=sorted(L)

def merge(L1,L2):
    lenL1 = len(L1)
    lenL2 = len(L2)
    print lenL1,lenL2
    i = 0
    j = 0
    L3 = []
    while j<lenL2 and i<lenL1:
        #print i,j
        if L1[i] == L2[j][1]:
            L3.append(L2[j][3].replace(' dBm',''))
            i +=1
            j +=1
        elif L1[i] < L2[j][1]:
            L3.append('0')
            i +=1
        else:
            j +=1
    while i<lenL1:
        L3.append('0')
        i +=1
    return L3         

#with open('extracted.csv', 'w') as out_file:
 #               	writer = csv.writer(out_file)
  #                      writer.writerow(tuple(temp))

dict = {'401':'C1','405':'C3','406':'C4','408':'C6','411':'C7','428':'C6','431':'C4','ds':'C1','fl':'C7','nw':'C4',
'oa':'C5','t':'C8','l':'C2'}

for dirpath, dirs, files in os.walk(fvGen):
    for filename in fnmatch.filter(files, '*.txt'):
         print filename
         with open(os.path.join(dirpath, filename)) as in_file:
                stripped = (line.strip() for line in in_file)
    		lines = (line for line in stripped if line)
    		grouped = zip(*[lines] * 6)
    		gro = grouped[1:len(grouped)]
    		gro = sorted(gro, key=lambda tup:tup[1])
		key= filename.split(" ")[0]
    		temp = merge(L,gro)+[dict[key]]
    		with open(saveAs, 'a+') as out_file:
                	writer = csv.writer(out_file)
                        writer.writerow(tuple(temp))

