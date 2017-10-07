# Change Return Program

# One thousand two hundred seventy dollars and twenty-eight cents.
#
# total cost = 29.7
# pay = 30
# change = 0.3




def change(cost, paid):

    if(cost < paid):
        change = str(round(cost - paid, 2))


        change = change.split('.')

        changeAmount = change


        return changeAmount;
    else:
        print('Money is not enough')

while True:
    try:
        cost = float(input('Please enter the cost of the product'))
        payment = float(input('Please enter customer paid'))
        break
    except:
        print('Please enter a valid amount')
        continue



changeAmount = change(cost, payment)
print('Change = Dollar: {} Cents {}'.format(abs(int(changeAmount[0])), changeAmount[1]) );
