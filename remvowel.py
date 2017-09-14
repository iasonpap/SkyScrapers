def disemvowel(string):
    string_ = list(string)
    print(string_)
    print("string={0}  list={1}".format(len(string), len(string_)))
    i = 0
    while i < len(string):
        if string_[i] == ('e' or "a" or "i" or "o" or "u" or "y"):
            string_.remove(string_[i])
            print("{0}".format(i))
        i += 1
    print(string_)
    new_str = ''.join(string_)
    return new_str


print(disemvowel("Hello World!"))
