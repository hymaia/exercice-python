import sys
import string
from collections import Counter


def main():
    input_str = sys.argv[1]
    cleaned_input = clean_text(input_str)
    print(wordcount(cleaned_input))


def clean_text(input_str: str) -> str:
    txt = input_str.translate(input_str.maketrans('', '', string.punctuation))
    return txt.lower()


def wordcount(input_str: str):
    word_list = input_str.split()
    return Counter(word_list).most_common()


if __name__ == "__main__":
    main()
