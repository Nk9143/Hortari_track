candidates=['Naveen','Sanjay','Naveen','Vishnu','Harsha','Naveen','Sanjay','Sanjay','Vishnu','Harsha','Harsha']
cand_temp={}
for candidate in candidates:
    if cand_temp.get(candidate)==None:
        cand_temp[candidate]=1
    else:
        cand_temp[candidate]+=1
for temp in sorted(cand_temp.keys()):
    if cand_temp[temp]==max(cand_temp.values()):
        winner=temp
print(winner)