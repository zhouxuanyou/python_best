from functools import reduce

tem = {'0':0,'1':1,'2':2}

def value(s):
    return tem[s]

res1 = list(map(value,'102'))
print(res1)

#转化整数
res2 = reduce(lambda x,y: 10*x+y,map(value,'102'))
print(type(res2))