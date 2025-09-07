def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents




def main():
    import sys
    from stats import sort_characters
    from stats import char_counting
    from stats import word_counting
    #filepath = "/home/roktor/workspace/github.com/ultra516/bookbot/books/frankenstein.txt"
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    content = get_book_text(filepath)
    #print(content)
    num_of_words = word_counting(content)
    count = char_counting(content)
    sorted_chars = sort_characters(count)
    #print(f"{num_of_words} words found in the document")
    #print (new_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()


