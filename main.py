from stats import get_num_words, get_num_chars, sort_char_list
import sys

def get_book_text(file_path):
    with open(file_path) as book_file:
        return book_file.read()

def main():

    if(len(sys.argv)<2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text=get_book_text(sys.argv[1])
    word_count=get_num_words(text)
    print(f"============ BOOKBOT ============\n"\
        f"Analyzing book found at {sys.argv[1]}...\n"\
        "----------- Word Count ----------\n"\
        f"Found {word_count} total words\n--------- Character Count -------" )
    char_count = get_num_chars(text)
    char_count_sorted = sort_char_list(char_count)

    for cur_char in char_count_sorted:
        print(f"{cur_char['char']}: {cur_char['count']}")

    print("============= END ===============")


main()