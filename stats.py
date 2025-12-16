def word_quantity(words):
    quantity = len(words)
    return quantity

def count_char(words):
    characters = {}
    for word in words:
        word = word.lower()
        for char in word:
            if char in characters:
                characters[char] += 1
            elif char == " " or char == "\n":
                continue
            else:
                characters[char] = 1
    return characters

def sort_on(items):
    return items["num"]

def list_counts(dictionary):
    chars = []
    for char in dictionary:
        chars.append({"char": char, "num": dictionary[char]})
    chars.sort(reverse = True, key=sort_on)
    return chars

def report(filepath, total_words, sorted_list):
    letters = ""
    for i in range(0, len(sorted_list)):
        letters += sorted_list[i]["char"] + ": " + str(sorted_list[i]["num"]) + "\n"
    
    output = f"""
============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {total_words} total words
--------- Character Count -------
{letters}
============= END ===============
    """
    return output