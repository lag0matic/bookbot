import sys
from stats import count_words, char_count, get_book_text ,sort_char_count



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    print(f'Analyzing book found at {book_path}')
    print("----------- Word Count ----------")
    print(f'Found {count_words(book_text)} total words')
    print("--------- Character Count -------")
    counted = char_count(book_text)
    sorted = sort_char_count(counted)
    for char in sorted:
        print(f'{char[0]}: {char[1]}')
    print("============= END ===============")
    

main()
