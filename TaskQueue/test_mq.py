import mq
from mq import Mq
import json

m = Mq('test')

a = {"reportid": 1, "name": "aroba", "age": 22, "friends": 3}
b = {"reportid": 2, "name": "brob", "age": 23, "friends": 4}
c = {"reportid": 3, "name": "robin", "age": 24, "friends": 23}

Mq('test').put(a)
m.put(b)
m.put(c)
print m.get()
print m.peek(2)
print m.find(1)
print m.get()


m.delete(3)
print m.qsize()
m.clear()

