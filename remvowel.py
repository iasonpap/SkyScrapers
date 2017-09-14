def disemvowel(str2handle):
    vowel_character = ["a", "A", "e", "E", "o", "O", "i", "I", "u", "U"]
    str2return = ""
    i = 0
    n = len(str2handle)
    while i < n:
        if not str2handle[i] in vowel_character:
            str2return += str2handle[i]
        i += 1
    return str2return

print(disemvowel("input("Type your word here: ")"))
