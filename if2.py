def main(one, two):
    if type(one) !=str or type(two) != str:
        return '0'
    elif one == two:
        return 1
    elif one != two:
        if two == "learn":
            return 3
        else:
            if len(one) > len(two):
                return 2

    return "Измени пааметры!"

print(main("ПРИВЕТ","ХЭЙ"))