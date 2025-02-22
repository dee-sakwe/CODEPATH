# Do you love the way I do when I'm loving your body?

def nanana_batman(x):
    # Understand: I'm expected to return the batman song
    # "na" is printed x times and concatenated with "Batman"
    # 1 <= x <= inf


    # Match: Simple for loop should work
    # Plan: initialize result variable with an empty string
    # then use the for loop to continually add "na" to our string

    # Implement:
    result = " Batman"

    for _ in range(x):
        result = "na" + result


    return result.strip()


    '''
    result = ""

    for _ in range(x):
        result += "na"

    return result + " Batman"
    '''


print(nanana_batman(0))