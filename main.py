from stats import word_quantity
from stats import count_char
from stats import list_counts
from stats import report

FILEPATH = "books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    content = get_book_text(FILEPATH)
    words = content.split()
    quantity = word_quantity(words)
    dictionary = count_char(content)
    sorts = list_counts(dictionary)
    pretty = report(FILEPATH, quantity, sorts)
    print(pretty)
main()