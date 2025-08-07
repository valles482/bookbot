from stats import get_num_words
from stats import count_characters
from stats import sort_dictionary
import sys

def check_args():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as file:
        text = file.read()
    return text

def main():
    filepath = check_args()
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    num_words = get_num_words(filepath)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_counts = count_characters(filepath)
    sorted_counts = sort_dictionary(char_counts)
    for char, count in sorted_counts.items():
        print(f"{char}: {count}")
    print("============= END ===============")
if __name__ == "__main__":
    main()