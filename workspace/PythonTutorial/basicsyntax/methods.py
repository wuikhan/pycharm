def sum_nums(num1, num2):
   return num1 + num2

sum = sum_nums(2, 8)
print(sum)


def isMetro(cityName):
    l = ['sfo', 'nyc', 'la']

    if cityName in l:
        return True
    else:
        return False

x = isMetro('boston')
print(x)