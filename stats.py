def count_words(book_text):
    words = book_text.split()
    return len(words)

def char_count(book_text):
    char_list = dict()
    for letter in book_text:
        letter = letter.lower()
        if letter in char_list:
            char_list[letter] += 1
        else:
            char_list[letter] = 1
    return char_list

def get_book_text(path):   
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def sort_on(item):
    return item[1]


def sort_char_count(counted):
    chars = list(counted.items())
    sorted_list = sorted(chars, reverse=True, key=sort_on)
    return sorted_list