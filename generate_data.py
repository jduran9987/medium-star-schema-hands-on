""" 
generate Users, Orders, Executions, Symbols
table data
"""
from faker import Faker
import csv
from datetime import date
import random

faker = Faker()

# Reproduce the same random data used in the tutorial
Faker.seed(0)

# create 50 fake users 
user_created = {} # store user_id along with the account created date

with open('users.csv', 'w') as f:
    csvwriter = csv.writer(f)
    header = ['user_id', 'first_name', 'last_name', 'email', 'city', 'state', 'date_joined']

    for i in range(51):
        if i == 0:
            csvwriter.writerow(header)
            continue

        user_id = i
        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()
        city = faker.city()
        state = faker.state()
        account_creation = faker.date_between_dates(
            date_start=date(2019, 1, 1),
            date_end=date(2020,1, 1)
        )

        user_created[user_id] = account_creation
        csvwriter.writerow([user_id, first_name, last_name, email, city, state, account_creation])

# create 20 symbols
exchanges_list = ['exchange1', 'exchange2']
symbol_list = []

with open('symbols.csv', 'w') as f:
    csvwriter = csv.writer(f)
    header = ['symbol_id', 'symbol', 'date_added', 'listed_at']
    
    for i in range(20):
        if i == 0:
            csvwriter.writerow(header)
            continue

        symbol_id = i
        
        while True:
            symbol = faker.lexify(text='??', letters='ABCDEFGHIJKLKMN')
            if symbol in symbol_list:
                continue 
            else:
                break

        date_added = faker.date_between_dates(
            date_start=date(2000, 1, 1),
            date_end=date(2020,1, 1)
        )
        listed_at = random.choice(exchanges_list)

        symbol_list.append(symbol)
        csvwriter.writerow([symbol_id, symbol, date_added, listed_at])

# create 1000 orders 
with open('orders.csv', 'w') as f:
    csvwriter = csv.writer(f)
    header = ['order_id', 'user_id', 'symbol_id', 'price', 'quantity', 'order_date', 'buy_or_sell', 'order_status']

    for i in range(1001):
        if i == 0:
            csvwriter.writerow(header)
            continue

        order_id = i 
        user_id = random.randint(1, 50)
        symbol_id = random.randint(1,19)
        price = random.randint(10, 200)
        quantity = random.randint(1,15)
        order_date = faker.date_between_dates(
            date_start=user_created[user_id],
            date_end=date(2021, 2, 1)
        )
        buy_or_sell = random.choice(['buy', 'sell'])
        order_status = random.choice(['executed', 'canceled'])
        
        csvwriter.writerow([order_id, user_id, symbol_id, price, quantity, order_date, buy_or_sell, order_status])
