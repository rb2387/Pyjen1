import datetime

print(datetime.datetime.now())

### ALLOCATION

name = input("Please specify your name : ")

def table(name):
    if name[0].lower() < 'm':
        print("Go to table A")
    else:
        print("Go to table B")

table(name)