

def primeNumCheck(amount):
    primeList = [2]
    pastList = []
    for num in range(2, amount):
        if(pastList):
            for past in pastList:
                if(num % past == 0):
                    break
            else:
                primeList.append(num)

        pastList.append(num)

    return primeList;


def primeFactorCheck(number):
    factorList = []
    pastList = []
    for num in range(2, number):
        pastList.append(num)

    for past in pastList:
        if(number % past == 0):
            factorList.append(past)

    return factorList;


while(True):
    try:
        inputVal = int(input('Please enter a number, and I will find you all prime factor'))
        break
    except:
        continue


resultList = [];

primeList = primeNumCheck(inputVal);

factorList = primeFactorCheck(inputVal);

print('Prime List: ' , primeList);

for factor in factorList:
    try:
        if(primeList.index(factor)):
            resultList.append(factor)

    except:
        pass

# print('Result: ' , resultList);
