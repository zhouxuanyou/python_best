import hashlib

num = 'abs2211'

def hashmd5(i):
    res = hashlib.md5(i).hexdigest()
    return res

def hashsha256(i):
    res = hashlib.sha256(i).hexdigest()
    return res

if __name__ == '__main__':
    #进行哈希散列时要注意编码问题
    print(hashmd5(num.encode('utf-8')))
    print(hashsha256(num.encode('utf-8')))