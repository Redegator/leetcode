def fractionAddition(expression: str) -> str:

    res = "0/1"

    if expression[0] != "-":
        expression = "+" + expression

    pos_of_digits = []
    for symbol_number in range(len(expression)):
        if expression[symbol_number] == "+" or expression[symbol_number] == "-":
            pos_of_digits.append(symbol_number)

    list_numerators = []
    list_denominators = []


    start = 0
    pos_of_digits.append(len(expression))
    for position in pos_of_digits[1::]:
        end = position

        lenght_between_start_end = end - start
        operation = expression[start]


        if expression[start+2] == "/":
            numerator = int(expression[start+1])
            if lenght_between_start_end == 4:
                denominator = int(expression[start+3])
            else:
                denominator = 10

        elif expression[start+3] == "/":
            numerator = 10
            if lenght_between_start_end == 5:
                denominator = int(expression[start+4])
            else:
                denominator = 10

        if operation == "-":
            numerator *= -1


        list_numerators.append(numerator)
        list_denominators.append(denominator)

        start = end

    multiplied_denominators = 1
    for x in list_denominators:
        multiplied_denominators *= x

    res_numerator = 0
    for i in range(len(list_numerators)):
        res_numerator += int(list_numerators[i] * multiplied_denominators / list_denominators[i])


    if res_numerator != 0:
        i = 10
        while i > 1:
            if res_numerator % i == 0 and multiplied_denominators % i == 0:
                res_numerator //= i
                multiplied_denominators //= i
            else:
                i -= 1

        res = str(res_numerator) + "/" + str(multiplied_denominators)

    return res


expression = "-5/2+10/3+7/9"
print(fractionAddition(expression))

