temp={}
print(type(temp))
temp['ram']=30
temp['sohan']=55
temp['rohan']=50
print(temp)

dic={"mohan":"Lg","ram":"Samsung"}
print(dic)

print(temp.keys())
print(temp.values())

print(temp['ram'])

s=dict()
print(type(s))

print(s)

s=dict(temp)
print(s)

del temp['ram']
print(temp)

print('sohan1' in temp)