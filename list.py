batches=["PPA","LB","Angular","Python"]
'''
print(batches)
print(batches[0])
print(batches[1])
print(batches[-1])
print(batches[1:])
print(batches[:3])

print(batches[-1])
print(batches[-2])
print(batches[-3])
print(batches[-4])

print(batches[1:])
print(batches[2:])
print(batches[3:])
print(batches[4:])

print(batches[:0])
print(batches[:1])
print(batches[:2])
print(batches[:3])
print(batches[:4])

'''
data1=[11,"Marvellous",3.14]
print(data1)

data2=[21,"Infosystem",7.10]
print(data2)

combined=[data1,data2]
print(combined)

batches.append("Mean");
print(batches);

batches.insert(2,"LSP");
print(batches);

batches.remove("LSP");
print(batches);

batches.pop();
print(batches);

batches.pop(2);
print(batches);

del batches[1:]
print(batches)

batches.extend(["LB","PYTHON","ANGULAR","MEAN"]);
print(batches)

batches.sort()
print(batches);