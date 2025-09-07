def word_counting(content):
    words = content.split()
    num_of_words = 0
    for word in words:
        num_of_words += 1
    return num_of_words

def char_counting(content):
    count: dict[str, int] = {}
    for char in content.lower():
        if char in count:
            count[char] += 1
        else:
           count[char] = 1
    return count 

def sort_characters(counts):
    char_list: list[dict[str, int]] = []
    for char, num in counts.items():
        if char.isalpha() == True:
            char_list.append({"char": char, "num": num})
    def sort_key(item: dict[str, int]) -> int:
        return item["num"]
    char_list.sort(key=sort_key, reverse=True)

    return char_list