# Mortgage Calculator

principal = int(input('Enter the principal amount :'))

annual_interest_rate = float(input('Enter the rate of interest amount :'))

payment_term = int(input('Enter the number of years amount :'))


# Converting year and annual interest to monthly
term_in_months = payment_term * 12

monthly_interest_rate = annual_interest_rate / 1200

# Formula
monthly_payment = principal*((monthly_interest_rate*((1+monthly_interest_rate)**term_in_months))/(((1+monthly_interest_rate)**term_in_months)-1))

print('')
print('---------------------')
print('Details')
print('---------------------')
print(f'Principal Amount is ${round(principal)}')
print(f'Annual rate of interest is {round(annual_interest_rate)}%')
print(f'Tenure is {round(payment_term)}yrs')
print(f'Monthly EMI is ${round(monthly_payment)}')