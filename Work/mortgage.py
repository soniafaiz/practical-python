# mortgage.py
#
# Exercise 1.7 & 1.8

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
paymentCount = 0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    if paymentCount < 12:
        principal -= 1000
        total_paid += 1000
    paymentCount += 1

print('Total paid is {:,.2f} over {} months.'.format(total_paid, paymentCount))
