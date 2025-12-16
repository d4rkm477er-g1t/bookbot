## USAGE: RUN python3 main.py <path_to_book>
##<path_to_book> should be a .txt file


from stats import word_quantity
from stats import count_char
from stats import list_counts
from stats import report
import sys





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


try:
    if len(sys.argv) == 2:
        FILEPATH = sys.argv[1]
        main()
    else:
        raise Exception
except Exception:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)