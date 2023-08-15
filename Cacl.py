import datetime

print(datetime.datetime.now())

def even(rbg):
    c = []
    for i in rbg:
        if i%2 ==0:
            c.append(i)
        else:
            pass
    return c
d = list(range(1,20))

print(even(range(20)))