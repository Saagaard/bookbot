import sys
from stats import get_word_count
from stats import get_character_count
from stats import sort_dictionary
from stats import print_sorted_dictionary


def get_book_text(filepath):
    contents = ""
    with open(filepath) as f:
        contents = f.read()
        #print(contents)
    return contents
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_contents = get_book_text(sys.argv[1])
    word_count = get_word_count(book_contents)
    character_count = get_character_count(list(book_contents.lower()))
    print(f"Found {word_count} total words")
    #print(character_count)
    sorted = sort_dictionary(character_count)
    print_sorted_dictionary(sorted)


main()