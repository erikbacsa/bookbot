from stats import *
import sys

def get_book_text(filepath):
    file = open(filepath, "r")
    text = file.read().strip()
    file.close()
    return text

def print_text(filepath, num_words, sorted_letters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print(f"----------- Word Count ----------\nFound {num_words} total words")
    print("--------- Character Count -------")
    print_sorted_letters(sorted_letters)
    
def get_sys_argv():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]
    
    

def main():
    filepath = get_sys_argv()
    text = get_book_text(filepath)
    
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    sorted_letters = sort_letters(num_letters)
    
    
    # Print stuff
    print_text(filepath, num_words, sorted_letters)
    
if __name__ == "__main__":
    main()