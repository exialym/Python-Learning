a = {'food': 'egg', 'level': 1 ,'color': 'red'}
b = {}
b['name'] = 'bob'
b['age'] = 23
b['job'] = 'dev'
print(a)
print(b)
c = {'name': {'last': 'ym', 'first': 'l'},
     'job': ['dev', 'mgr'],
     'age': 22}
print(c)
print(c['name']['last'])
print(c['job'][:])
c['job'].append('CEO')
print(c)
#cKey = c.keys()
#cKey.sort()
#print(cKey)
for key in sorted(c):
    print(key,'=>',c[key])
if not 'sex' in c:
    print("no such item")
print(c.get("sex",0))
print(c["sex"] if 'sex' in c else 0)



