string='My name is nitin my , nitin'
def unique_string():
    word = set()
    for _ in range(1000):
        word.add(unique_string())
    return word

unique_string()



a=(2)
print(type(a))