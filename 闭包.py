import time
def lazyfn(*args):
    starttime = time.clock()
    def myfn():
        cnt = 0
        for i in args:
            cnt += i
        return cnt
    endtime = time.clock()
    tm = endtime - starttime
    print(tm)
    return myfn

a = lazyfn(*range(10000001))
print(a)
print(a())

