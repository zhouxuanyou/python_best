def pr_3(i):
    print(i)
    i += 1
    if i <= 3:
        pr_3(i)
    print(i - 1)

#阶梯乘法
def calNum(i):
    if i == 1:
        return 1
    else:
        return i * calNum(i-1)

#斐波拉契数列
def feibo(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return feibo(i-1)+feibo(i-2)
if __name__ == '__main__':
    print(feibo(3))