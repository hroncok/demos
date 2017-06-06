def fizzbuzz(num):
    if (num % 15) == 0:
        return 'fizzbuzz'
    if (num % 5) == 0:
        return 'buzz'
    if (num % 3) == 0:
        return 'fizz'
    return str(num)
