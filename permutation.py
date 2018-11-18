from itertools import permutations
int_str='123'
temp=list(permutations(int_str))
arr=[int(''.join(a)) for a in temp]
for ar in arr:
    if ar%8==0:
        print(ar)