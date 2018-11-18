arr=[5,2,3,6,5,8,9,6,4,7,5,6,7,5]
count={}
for a in arr:
    if count.get(a)==None:
        count[a]=1
    else:
        count[a]+=1
dup=[a for a in count.keys() if count[a]>=2]
print("Number of duplicate elements",len(dup))
print("The duplicte elements are",dup)
print("Array without duplicate elements",list(count.keys()))

    