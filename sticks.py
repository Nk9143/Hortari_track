length=int(input("enter number of sticks:"))
sticks=[int(input("enter stick "+str(l)+" length:")) for l in range(1,length+1)]
count=[]
while len(sticks)>=1:
    count.append(len(sticks))
    minimum=min(sticks)
    temp=[stick-minimum for stick in sticks] 
    sticks.clear()
    for x in temp:
        if x>=1:
            sticks.append(x)
    temp.clear()            
print(count)
