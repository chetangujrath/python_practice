
def convert_upper(func):
    def wrapper(word):
        return func(word).upper()
    return wrapper

def convert_lower(func):
    def wrapper(word):
        return func(word).lower()
    return wrapper

@convert_upper
def show_word(word):
    return word

print(show_word("chetan"))

@convert_lower
def show_word(word):
    return word

print(show_word("CHETAN"))