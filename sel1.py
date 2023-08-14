import pandas
import datetime
import numpy as np


print(f' Welcome : {datetime.datetime.now()}')
print("Logs enabled")


x = np.random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(1))

print(x)

shoes = {'name': 'Fancy Shoes ' , 'price':14900}

def applydisc(product , discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price

amount = applydisc(shoes,.30)
print(amount)
