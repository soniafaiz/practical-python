# mortgage.py
#
# Exercise 1.7, 1.8, 1.9, 1.10, 1.11

principal = 500000.0
rate = 0.05
payment = 2684.11
payment_for_month = 0.0
total_paid = 0.0
paymentCount = 0

extra_payment_start_month = int(input('Enter the month to start the extra payment:'))
extra_payment_end_month = int(input('Enter the month to end the extra payment:'))
extra_payment = int(input('Enter the extra payment:'))

while principal > 0:

    if (paymentCount >= extra_payment_start_month-1) and (paymentCount < extra_payment_end_month-1):
        payment_for_month = payment + extra_payment
    else:
        payment_for_month = payment

    if payment_for_month > principal*(1+rate/12):
        payment_for_month = principal * (1+rate/12)

    principal = principal * (1+rate/12) - payment_for_month
    total_paid = total_paid + payment_for_month
    paymentCount += 1
    print('{:3d} {:9.2f} {:9.2f}'.format(paymentCount, total_paid, principal))

print('Total paid is {:,.2f} over {} months.'.format(total_paid, paymentCount))
