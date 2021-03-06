#!/usr/bin/python

cnt = 50

class InstanceCounter:
    count = 0

    def __init__(self, val):
        self.val = val
        global cnt
        cnt += 1
        print(cnt)

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    def get_count(self):
        return InstanceCounter.count


a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

for obj in (a,b,c):
    print( f'val of obj: {obj.get_val()}' )
    print( f'count: {obj.get_count()}' )