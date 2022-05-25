# mortgage.py
#
# Exercise 1.7, 1.8, 1.9

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
paymentCount = 0

extra_payment_start_month = input('Enter the month to start the extra payment:')
extra_payment_end_month = input('Enter the month to end the extra payment:')
extra_payment = input('Enter the extra payment:')

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    if (paymentCount >= extra_payment_start_month-1) and (paymentCount < extra_payment_end_month-1):
        principal -= extra_payment
        total_paid += extra_payment
    paymentCount += 1
    print('{:3d} {:9.2f} {:9.2f}'.format(paymentCount, total_paid, principal))

print('Total paid is {:,.2f} over {} months.'.format(total_paid, paymentCount))
