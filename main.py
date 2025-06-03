import sys

from stats import count_chars, count_words, sort_chars


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_fp = sys.argv[1]

    text = get_book_text(book_fp)
    words = count_words(text)
    chars = count_chars(text)
    sorted = sort_chars(chars)
    print_report(book_fp, words, sorted)


def get_book_text(filepath: str):
    with open(filepath) as f:
        return f.read()


def print_report(book_fp: str, word_count: int, sorted_chars: dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_fp}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        if char.isalpha():
            print(f"{char}: {sorted_chars[char]}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
