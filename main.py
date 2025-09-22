import sys


def get_book_text(file_path):

    with open(file_path) as f:
        return f.read()

from stats import get_word_count

from stats import get_char_count

from stats import sort_on

from stats import char_dict_to_sorteed_list


def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    else: 
        book_path = sys.argv[1]


    text = get_book_text(book_path)
    num_words = get_word_count(text)
    

    char_count = get_char_count(text)
    #print(char_count)

    list_dict = char_dict_to_sorteed_list(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    print("--------- Character Count -------")
    for char in list_dict:
        if char["char"].isalpha():
            print(char["char"] + ":" + " " + str(char["num"]))
    print("============= END ===============")


main()