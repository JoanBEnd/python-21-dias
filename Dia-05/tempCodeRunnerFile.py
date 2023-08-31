

def find_largest_palindrome(words):
    output = None

    for items in words:
        new_texto =""
        for caracter in reversed(items):
            new_texto += caracter

        if new_texto == items:
            if output == None:
                output = new_texto
            elif len(new_texto) > len(output):
                output = new_texto

    print(output)


find_largest_palindrome(["racecar", "level", "world", "hello"])
find_largest_palindrome(["Platzi", "Python", "django", "flask"])