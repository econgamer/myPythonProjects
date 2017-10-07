pi = '3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481 ';

def piToNDigit(n):
    result = [];
    for i in range(n):
        result.append(pi[i])

    return result


while True:
    try:
        inputVal = int(input('Please  Enter a number and have the program generate PI up to that many decimal places, 100 is the maximum : '));



    except:
        continue

    if inputVal <= 100:
        result = piToNDigit(inputVal+2)
        result = ''.join(result)
        print(result)
        break
    else:
        continue
