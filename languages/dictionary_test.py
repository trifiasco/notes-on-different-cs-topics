

mp = dict()

for i in range(5):
    if i not in mp:
        mp[i] = 1
    
    print(mp[i])

for i in range(10):
    if mp.get(i, 0) == 0:
        mp[i] = 0
    else:
        mp[i] += 1
    
    print(mp[i])
