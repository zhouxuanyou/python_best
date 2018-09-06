# import socket
#
# sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# addr = ('0.0.0.0',)
from functools import reduce
a = sum([ i for i in range(1,101) if not i%2==0])
b = reduce([ i for i in range(1,101) if  i%2==0],lambda x:x+i)
print(a)