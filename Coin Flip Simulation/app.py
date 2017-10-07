import random

def coinFlip(times):
    coinList = [];
    for flip in range(times):
        randomNum = random.randint(1, 2)
        coinList.append(randomNum)
    return coinList

try:
    inputVal = int(input('Please enter the number of times you wanna flip'))
except:
    print('I expect a number')

myGenerator = coinFlip(inputVal)


tails = 0
heads = 0

for i in myGenerator:
    if i == 1:
        tails = tails + 1
    else:
        heads = heads + 1
    print(i)

print("Total number of tails " , tails)
print("Total number of heads " , heads)
