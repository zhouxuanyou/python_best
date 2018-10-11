# a  = [1,5,2,1,9,1,5,10]
# # def duupe(items):
# #     seen = set()
# #     for item in items:
# #         if item not in seen:
# #             yield item
# #             seen.add(item)
# #
# # b = list(duupe(a))
# # print(b)
# import re
#
# line = "asdf,fjdk af*ed;fjek,asdf_foo"
# print(re.split(r'[;,\s]s*',line))
# a0 = dict(zip(('a','b','c'),(1,2,3)))
# print(a0)
# print(range(6))
# a3 = [a0[s] for s in a0]
# print(a3)
a = [{'x':1,'y':2},{'x':1,'y':3},{'x':1,'y':2},{'x':2,'y':4}]
def duupe(items,key=None):
     seen = set()
     for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

b = list(duupe(a,key=lambda d:(d['x'],d['y'])))
c = list(duupe(a,key=lambda d:d['x']))
print(b)
print(c)