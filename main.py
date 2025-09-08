from stats import get_book_words, get_char_presence, structure_data
import sys

def main():
    if (len(sys.argv) != 2):
        print("Specify the relative path to the text file you " \
        "wanna analyze when running the program like this. " \
        "Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    else:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")

        text = get_books_text(sys.argv[1])
        nbr_of_words = len(get_book_words(text))
        print(f"Found {nbr_of_words} total words")

        print("--------- Character Count -------")
        chars = get_char_presence(text)
        char_info = structure_data(chars)

        for i in range(0, len(char_info)):
            if char_info[i]["char"].isalpha():
                print(f"{char_info[i]["char"]}: {char_info[i]["num"]}")

        print("============= END ===============")

def get_books_text(filepath):
    with open(filepath) as f:
        return f.read()
    
main()