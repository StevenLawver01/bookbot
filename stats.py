def get_word_count(text):

    num_words = text.split()
    return len(num_words)

def get_char_count(text):

    char_count = {}

    for char in text:
        char = char.lower()
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    
    return char_count


def sort_on(items):
    return items["num"]

def char_dict_to_sorteed_list(char_counts):
    
    list_dict = list()

    for char in char_counts:
        list_dict.append({"char": char, "num": char_counts[char]})

    list_dict.sort(reverse=True, key=sort_on)
    return list_dict

