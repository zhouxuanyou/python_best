


with open('/Users/zhouxuanyou/PycharmProjects/python_best/test.txt','r',encoding='utf-8')as f:
    a = f.readlines()
    b = [i.strip() for i in a]
    res = sorted(b, key=lambda x:x[-1],reverse=True)
    print(res)