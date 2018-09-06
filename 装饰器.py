


def factory(old_fn):
    def new_fn():
        print('*'*10)
        old_fn()
        print('*'*10)
    return new_fn

@factory
def fn():
    print('sakdjlaksdjasjdkajl')

#时间装饰器
def time_fatory(old_fn):
    import time
    def new_fn(*args,**kwargs):
        startime = time.clock()
        ret = old_fn(*args,**kwargs)
        endtime = time.clock()
        print('{} fun run {} seconds'.format(old_fn.__name__,endtime - startime))
        return ret
    return new_fn

#平方和
@time_fatory
def sub_statcis(arg):
    cnt = 0
    for i in arg:
        cnt += i * 2
    return cnt

def main_test():
    data = range(1,100)
    res = sub_statcis(data)
    print('res 1-100:%s'%res)

    data = range(1, 100000001)
    res = sub_statcis(data)
    print('res 1-100000001:%s' % res)

if __name__ == '__main__':
    main_test()